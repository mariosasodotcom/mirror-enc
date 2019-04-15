#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64
import os

def enc_dec():
    print("\n    [1.] Encode to Base64")
    print("    [2.] Decode from Base64")
    print("    [CTRL + C] EXIT mirror-enc")
    x = '0'
    while x not in ['1', '2']:
        x = str(raw_input("\nmirror-enc > "))
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
