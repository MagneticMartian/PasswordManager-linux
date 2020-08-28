import argparse
import sys
import os
import string
import random
import h5py

db_str = '/home/chrid/PasswordManager/pass_db.hdf5'

def randomString(stringLength = 16):
    password_chars = string.ascii_letters + string.digits + string.punctuation
    pwd = ''.join(random.choice(password_chars) for i in range(stringLength))
    
    return pwd

def pass_db_create(url_str):
    if(os.path.exists(db_str)):
        print('Error: password bank already exist. Please use {--append}')
        sys.exit()
    
    f = h5py.File(db_str,'a')
    url_grp = f.create_group("URL_LIST")
    url_subgrp = url_grp.create_group(url_str[0].encode('ascii'))
    dset = url_subgrp.create_dataset("Password", (1,))

    if(len(url_str) != 1):
        dset.attrs["Password"] = url_str[1]
    else:
        pass_args = randomString()
        dset.attrs["Password"] = pass_args

def pass_db_append(url_str):
    f = h5py.File(db_str,'a')

    if(f["URL_LIST"]):
        url_grp = f["URL_LIST"]
        url = f.get("URL_LIST")

        if(url_str[0] in list(url.keys())):
            print('Error: web page already has a password. use {--read} to see')
            sys.exit()

        url_subgrp = url_grp.create_group(url_str[0].encode('ascii'))
        dset = url_subgrp.create_dataset("Password", (1,))

        if(len(url_str) != 1):
            dset.attrs["Password"] = url_str[1]
        else:
            pass_args = randomString()
            dset.attrs["Password"] = pass_args
            
    else:
        pass_db_create(url_str)

def pass_db_delete(url_str):
    f = h5py.File(db_str,'a')
    url_grp = f["URL_LIST"]
    del url_grp[url_str[0].encode('ascii')]

def pass_db_read (url_str):
    f = h5py.File(db_str,'r')
    check = f.get('URL_LIST')
    if(url_str[0] not in list(check.keys())):
        print('Error: web page does not exist.')
        sys.exit()
    data = f.get('URL_LIST/'+url_str[0]+'/Password')
    pwd = list(data.attrs.values())
    return pwd[0]

def pass_db_list(url_str):
    if(url_str[0] == "url"):
        f = h5py.File(db_str,'r')
        url_list = f.get('URL_LIST')
        return list(url_list.keys())
    else:
        sys.exit(1)

parser = argparse.ArgumentParser(description='Create and Parse Password data manager')
parser.add_argument('strings', metavar='URL',nargs='+',
                    help='URL for the accumulator')
parser.add_argument('--create',dest='accumulator',action='store_const',
                    const=pass_db_create, help='Need url to gen password')
parser.add_argument('--append',dest='accumulator',action='store_const',
                    const=pass_db_append, help='Need url to gen password')
parser.add_argument('--delete',dest='accumulator',action='store_const',
                    const=pass_db_delete, help='Need url to gen password')
parser.add_argument('--read',dest='accumulator',action='store_const',
                    const=pass_db_read, help='Need url to gen password')
parser.add_argument('--list',dest='accumulator',action='store_const',
                    const=pass_db_list, help='Need url to gen password')

args = parser.parse_args()
print(args.accumulator(args.strings))