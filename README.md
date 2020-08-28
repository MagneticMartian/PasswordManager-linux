This is the gnu/linux version of of the other password manager. The main differences are that this implementation is able to list all url's that it has a stored password, and it also encrypts the pass_db.hdf5 data base.

Dependency: ccrypt h5py

sudo apt install ccrypt

pip install h5py

Setup:

Run ./setup.sh

Operation:

passman is the only program that you will have to directly run.

usage passman:

passman [option] [args]

Options:
-e arg: If arg=NULL, passman encrypts the pass_db.hdf5 file. If arg=url,passman creates the pass_db.hdf5 file and then encrypts it.
-d args: passman will decrypt the pass_db.hdf5 file. The args variables are the [option] [url] arguments for pass_manager.py.

Usage pass_manager.py:

python3 pass_manager.py [option] [url] [new_password=null]

Options:

--create: Creates a new database initalized with [url] and [new_password] is optional

--append: add a new [url] with optional [new_password]

--delete: delete a previous [url]

--read: read password for [url]

--list url: lists out all url's currently stored in database.

URL:

This is not required to be a url. It can really be any string you wish. Just make sure that it is a good enough identifier. One where you can remember the web site that it is related to.

NEW_PASSWORD:

If no password is supplied the application will randomly generate a 16 ascii character string for you. Other wise, the application will store your supplied password.
