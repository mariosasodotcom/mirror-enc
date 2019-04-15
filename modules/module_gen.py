#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import string
import random
from Crypto.PublicKey import RSA

def open_dir():
    path = str(raw_input("\nDirectory path: "))
    if os.path.isdir(path) == True:
        return path
    print("This is not a directory or it does not exist")
    open_dir()
        
def menu():
    menu = """
    [1.] Generate AES-128 Key
    [2.] Generate AES-192 Key
    [3.] Generate AES-256 Key
    [4.] Generate RSA-1024 Keypair
    [5.] Generate RSA-2048 Keypair
    [6.] Generate RSA-4096 Keypair
    [CTRL + C] EXIT mirror-enc  
    """
    print(menu)
    x = '0'
    while x not in ['1', '2', '3', '4', '5', '6']:
        x = str(raw_input("mirror-enc > "))
    return x

def main(mode):
    choose = menu()

    if choose == '1':
        chars = string.letters + string.digits + string.punctuation
        key = "".join([random.choice(chars) for x in xrange(16)])
        print("\nAES-128 Key: " + key)

    elif choose == '2':        
        chars = string.letters + string.digits + string.punctuation
        key = "".join([random.choice(chars) for x in xrange(24)])
        print("\nAES-192 Key: " + key)

    elif choose == '3':        
        chars = string.letters + string.digits + string.punctuation
        key = "".join([random.choice(chars) for x in xrange(32)])
        print("\nAES-256 Key: " + key)

    elif choose == '4':
        directory = open_dir()
        os.chdir(directory)
        key = RSA.generate(1024)  
        f = open("pubKey.pem", 'wb')
        f.write(key.publickey().exportKey('PEM'))
        f.close
        f = open("prvKey.pem", 'wb')
        f.write(key.exportKey('PEM'))
        f.close
        print("\nRSA-1024 Keypair generated!")

    elif choose == '5':
        directory = open_dir()
        os.chdir(directory)
        key = RSA.generate(2048)  
        f = open("pubKey.pem", 'wb')
        f.write(key.publickey().exportKey('PEM'))
        f.close
        f = open("prvKey.pem", 'wb')
        f.write(key.exportKey('PEM'))
        f.close
        print("\nRSA-2048 Keypair generated!")

    elif choose == '6':
        directory = open_dir()
        os.chdir(directory)
        key = RSA.generate(4096)  
        f = open("pubKey.pem", 'wb')
        f.write(key.publickey().exportKey('PEM'))
        f.close
        f = open("prvKey.pem", 'wb')
        f.write(key.exportKey('PEM'))
        f.close
        print("\nRSA-4096 Keypair generated!")
            







