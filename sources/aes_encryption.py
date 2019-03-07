#!/usr/bin/env python

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
        key = str(raw_input("\nAES key encryption (128, 192 or 256 bits: "))
        bytes = len(key)

    return key



def enc_dec(key):

    msg = None

    if sys.argv[1] == '-t':

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
        x = str(raw_input("\nmirror-enc/aes > "))

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



def encrypt_list(files, key):

    for file in files:

        print("\nFile: " + os.path.abspath(file))

        try:

            with open(file, 'rb') as fopen:
                plaintext = fopen.read()

            chipertext = encrypt(plaintext, key)

            with open(file, 'wb') as fopen:
                fopen.write(chipertext)

            print("Encrypted")

        except:
            print("Not encrypted")



def decrypt_list(files, key):

    for file in files:

        print("\nFile: " + os.path.abspath(file))

        try:

            with open(file, 'rb') as fopen:
                chipertext = fopen.read()

            plaintext = decrypt(chipertext, key)

            with open(file, 'wb') as fopen:
                fopen.write(plaintext)

            print("Decrypted")

        except:
            print("Not Decrypted")



def encrypt_texts(texts, key):

    for text in texts:

        print("\nPlaintext: " + text)

        try:

            chipertext = encrypt(text, key)

            print("Ciphertext: " + base64.b64encode(chipertext))

        except:
            print("Not Encrypted")



def decrypt_texts(texts, key):

    for txt in texts:

        text = base64.b64decode(txt)

        print("\nCiphertext: " + txt)

        try:

            plaintext = decrypt(text, key)

            print("Plaintext: " + plaintext)

        except:
            print("Not Decrypted")








