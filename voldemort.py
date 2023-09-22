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
