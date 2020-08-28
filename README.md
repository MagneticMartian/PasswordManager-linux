This is a basic password management application. The executable in the repository is only good for Windows systems. It is currently not very secure at all. Other than the fact that not many people use hdf5 anymore. The interface is designed to be simple and intuitive.

Usage:

open terminal (cmd) and type:

cd C:\<path_to_exe_dir>

pass_manager.exe <option> <url> <new_password=null>

Options:

--create: Creates a new database initalized with <url> and <new_password> is optional

--append: add a new <url> with optional <new_password>

--delete: delete a previous <url>

--read: read password for <url>

--list url: lists out all url's currently stored in database.

URL:

This is not required to be a url. It can really be any string you wish. Just make sure that it is a good enough identifier. One where you can remember the web site that it is related to.

NEW_PASSWORD:

If no password is supplied the application will randomly generate a 16 ascii character string for you. Other wise, the application will store your supplied password.