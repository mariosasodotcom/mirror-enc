#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import algorithms.aes_encryption as aes_encryption
import algorithms.hash_algorithms as hash_algorithms
import algorithms.base64_encoding as base64_encoding


def open_bin():
    path = str(raw_input("\nFile path: "))
    if os.path.isfile(path):
        f = open(path, 'rb')
        binary = f.read()
        return binary, path
    print("This is not a file or it does not exist")
    open_bin()


def menu():
    menu_file = """
    [0.] RSA Encryption   [ Not available in file mode ]
    [1.] AES Encryption   [ AES-128, AES-192, AES-256 ]
    [2.] HASH Algorithms  [ MD5, SHA-1, SHA-224, SHA-256 ]
    [3.] BASE64 Encoding  [ FILE(S) <=> STRING(S) ]
    [CTRL + C] EXIT mirror-enc  
    """
    print(menu_file)
    x = ''
    while x not in ['1', '2', '3']:
        x = str(raw_input("mirror-enc > "))
    return x


def main(mode):
    choose = menu()

    if choose == '1':
        key = aes_encryption.choose_key()
        alg = aes_encryption.enc_dec(key, mode)
        binary, path = open_bin()
        if alg == "enc":
            try:
                cipher = aes_encryption.encrypt(binary, key)
                f = open(path, 'wb')
                f.write(cipher)
                print("\nEncrypted!")
            except:
                print("\nNot Encrypted!")
        elif alg == "dec":
            try:
                plain = aes_encryption.decrypt(binary, key)
                f = open(path, 'wb')
                f.write(plain)
                print("\nDecrypted!")
            except:
                print("\nNot Decrypted!")

    elif choose == '2':
        binary, path = open_bin()
        md5 = hash_algorithms.hash_md5(binary)
        sha1 = hash_algorithms.hash_sha1(binary)
        sha224 = hash_algorithms.hash_sha224(binary)
        sha256 = hash_algorithms.hash_sha256(binary)
        print("\nMD5: " + md5)
        print("SHA-1: " + sha1)
        print("SHA-224: " + sha224)
        print("SHA-256: " + sha256)

    elif choose == '3':
        alg = base64_encoding.enc_dec()
        binary, path = open_bin()
        if alg == "enc":
            try:
                encode = base64_encoding.base64_enc(binary)
                f = open(path, 'wb')
                f.write(encode)
                print("\nEncoded!")
            except:
                print("\nNot Encoded!")
        elif alg == "dec":
            try:
                decode = base64_encoding.base64_dec(binary)
                f = open(path, 'wb')
                f.write(decode)
                print("\nDecoded!")
            except:
                print("\nNot Decoded!")
