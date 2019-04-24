#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import algorithms.key_gen as key_gen


def open_dir():
    path = str(raw_input("\nDirectory path: "))
    if os.path.isdir(path):
        return path
    print("This is not a directory or it does not exist")
    open_dir()


def menu():
    menu_gen = """
    [0.] Generate RSA-1024 Keypair
    [1.] Generate RSA-2048 Keypair
    [2.] Generate RSA-4096 Keypair
    [3.] Generate AES-128 Random Key
    [4.] Generate AES-192 Random Key
    [5.] Generate AES-256 Random Key
    [CTRL + C] EXIT mirror-enc  
    """
    print(menu_gen)
    x = ''
    while x not in ['0', '1', '2', '3', '4', '5']:
        x = str(raw_input("mirror-enc > "))
    return x


def main():
    choose = menu()

    if choose == '0':
        directory = open_dir()
        os.chdir(directory)
        key_gen.rsa_gen(1024)
        print("\nRSA-1024 Keypair generated!")

    elif choose == '1':
        directory = open_dir()
        os.chdir(directory)
        key_gen.rsa_gen(2048)
        print("\nRSA-2048 Keypair generated!")

    elif choose == '2':
        directory = open_dir()
        os.chdir(directory)
        key_gen.rsa_gen(4096)
        print("\nRSA-4096 Keypair generated!")

    elif choose == '3':
        key = key_gen.aes_gen(16)
        print("\nAES-128 Key: " + key)

    elif choose == '4':
        key = key_gen.aes_gen(24)
        print("\nAES-192 Key: " + key)

    elif choose == '5':
        key = key_gen.aes_gen(32)
        print("\nAES-256 Key: " + key)
