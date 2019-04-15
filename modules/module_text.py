#!/usr/bin/env python
# -*- coding: utf-8 -*-

import algorithms.rsa_encryption as rsa_encryption
import algorithms.aes_encryption as aes_encryption
import algorithms.hash_algorithms as hash_algorithms
import algorithms.base64_encoding as base64_encoding

def menu():
    menu = """
    [0.] RSA Encryption   [ RSA-1024, RSA-2048, RSA-4096 ]
    [1.] AES Encryption   [ AES-128, AES-192, AES-256 ]
    [2.] HASH Algorithms  [ MD5, SHA-1, SHA-224, SHA-256 ]
    [3.] BASE64 Encoding  [ TEXT(S) <=> STRING(S) ]
    [CTRL + C] EXIT mirror-enc  
    """
    print(menu)
    x = ''
    while x not in ['0', '1', '2', '3']:
        x = str(raw_input("mirror-enc > "))
    return x

def main(mode):
    choose = menu()

    if choose == '0':        # RSA Encryption
        alg = rsa_encryption.enc_dec()
        key = rsa_encryption.choose_key(alg)
        string = raw_input("\nString: ")
        if alg == "enc":
            try:
                cipher = rsa_encryption.encrypt(string, key)
                print("\nChipertext: " + str(cipher))
            except:
                print("\nNot Encrypted!")
        elif alg == "dec":
            try:
                plain = rsa_encryption.decrypt(string, key)
                print("\nPlaintext: " + str(plain))
            except:
                print("\nNot Decrypted!")

    elif choose == '1':        # AES Encryption
        key = aes_encryption.choose_key()
        alg = aes_encryption.enc_dec(key, mode)
        string = str(raw_input("\nString: "))
        if alg == "enc":
            try:
                cipher = aes_encryption.encrypt(string, key)
                print("\nChipertext: " + base64_encoding.base64_enc(cipher))
            except:
                print("\nNot Encrypted!")
        elif alg == "dec":
            try:
                not_64 = base64_encoding.base64_dec(string)
                plain = aes_encryption.decrypt(not_64, key)
                print("\nPlaintext: " + plain)
            except:
                print("\nNot Decrypted!")

    elif choose == '2':        # HASH Algorithms
        string = str(raw_input("\nString: "))
        md5 = hash_algorithms.hash_md5(string)
        sha1 = hash_algorithms.hash_sha1(string)
        sha224 = hash_algorithms.hash_sha224(string)
        sha256 = hash_algorithms.hash_sha256(string)
        print("\nMD5: " + md5)
        print("SHA-1: " + sha1)
        print("SHA-224: " + sha224)
        print("SHA-256: " + sha256)

    elif choose == '3':        # Base64 Encoding 
        alg = base64_encoding.enc_dec()
        string = str(raw_input("\nString: "))
        if alg == "enc":
            try:
                encode = base64_encoding.base64_enc(string)
                print("B64 Encode: " + encode)
            except:
                print("\nNot Encoded!")
        elif alg == "dec":
            try:
                decode = base64_encoding.base64_dec(string)
                print("B64 Decode: " + decode)
            except:
                print("\nNot Decoded!")








