#!/usr/bin/env python


import base64
import os


def enc_dec():
    print("\n    [1.] Encode to Base64")
    print("    [2.] Decode from Base64")
    print("    [CTRL + C] EXIT mirror-enc")

    x = '0'

    while x not in ['1', '2']:
        x = str(raw_input("\nmirror-enc/base64 > "))

    if x == '1':
        return "enc"

    elif x == '2':
        return "dec"


def base64_enc(string):

    _str = base64.b64encode(string)

    return _str



def base64_dec(string):

    _str = base64.b64decode(string)

    return _str



def enc_texts(texts):

    for text in texts:

        print("\nString: " + text)

        try:

            _base64 = base64_enc(text)

            print("BASE64: " + _base64)

        except:
            print("Error")



def dec_texts(texts):

    for text in texts:

        print("\nBASE64: " + text)

        try:

            from_base64 = base64_dec(text)

            print("String: " + from_base64)

        except:
            print("Error")



def enc_files(files):

    for file in files:

        with open(file, 'rb') as fopen:
            bin_file = fopen.read()

        print("\nFile: " + os.path.abspath(file))

        try:

            _base64 = base64_enc(bin_file)

            with open(file, 'wb') as fopen:
                fopen.write(_base64)

            print("Encoded")

        except:
            print("Not encoded")



def dec_files(files):

    for file in files:

        with open(file, 'rb') as fopen:
            bin_file = fopen.read()

        print("\nBASE64: " + os.path.abspath(file))

        try:

            from_base64 = base64_dec(bin_file)

            with open(file, 'wb') as fopen:
                fopen.write(from_base64)

            print("Decoded")

        except:
            print("Not decoded")


