#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import base64
import sys
from Crypto import Random
from Crypto.Cipher import AES

def choose_key():
    key = str(raw_input("\nAES key encryption (128, 192 or 256 bits): "))
    bytes = len(key)
    valid_size = [16, 24, 32]
    while bytes not in valid_size:
        if bytes == 1:
            print("Error! Your key (1 byte) must be 16, 24 or 32 bytes long")
        else:
            print("Error! Your key (" + str(bytes) + " bytes) must be 16, 24 or 32 bytes long")
        key = str(raw_input("\nAES key encryption (128, 192 or 256 bits): "))
        bytes = len(key)
    return key

def enc_dec(key, mode):
    msg = None
    if mode == 't':
        msg = []
        msg.append(" (Output will be encoded with Base64)")
        msg.append(" (Input must be encoded with Base64)")
    else:
        msg = ["", ""]
    print("\n    [1.] Encrypt with AES-" + str(len(key) * 8) + msg[0])
    print("    [2.] Decrypt with AES-" + str(len(key) * 8) + msg[1])
    print("    [CTRL + C] EXIT mirror-enc")
    x = '0'
    while x not in ['1', '2']:
        x = str(raw_input("\nmirror-enc > "))
    if x == '1':
        return "enc"
    elif x == '2':
        return "dec"

def encrypt(plaintext, key):
    try:
        text = plaintext + b"\0" * (AES.block_size - len(plaintext) % AES.block_size)
        IV = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, IV)
        return IV + cipher.encrypt(text)
    except Exception as e:
        raise e

def decrypt(ciphertext, key):
    try:
        IV = ciphertext[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, IV)
        plaintext = cipher.decrypt(ciphertext[AES.block_size:])
        return plaintext.rstrip(b"\0")
    except Exception as e:
        raise e
