#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    Copyright (C) 2019 Mario Saso (github.com/M4R1OS4S0)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program. If not, see <https://www.gnu.org/licenses/>.


# Import statements
import os

# Import mirror-enc modules
from MirrorClass import *
from MirrorUtils import *


# Start file mode function
def FileMain():

    choose = ChooseMode(['1', '2', '3', '99'], file_menu)
    
    # AES Encryption
    if choose == '1':
    
        alg = ChooseMode(['0', '1', '99'], alg_menu)
        
        if alg == '99':
            return
        
        print(aes_file_help)
        
        key = AesChooseKey()      
        binary, path = OpenBin()
        
        if alg == '0':
        
            try:
                cipher = MirrorEnc(binary).AesEnc(key)
                open(path, 'wb').write(cipher)
                print("\nEncrypted! [{}]".format(path))
            except:
                print("\nNot Encrypted! [{}]".format(path))
                
        elif alg == '1':
            try:
                plain = MirrorEnc(binary).AesDec(key)
                open(path, 'wb').write(plain)
                print("\nDecrypted! [{}]".format(path))
            except:
                print("\nNot Decrypted! [{}]".format(path))
    
    # Hash Algorithms
    elif choose == '2':
    
        print(hash_file_help)
        binary, path = OpenBin()
       
        hashes = MirrorEnc(binary).GetHashes()
        
        print("\nMD5: " + hashes[0])
        print("SHA-1: " + hashes[1])
        print("SHA-224: " + hashes[2])
        print("SHA-256: " + hashes[3])

    # Base64 Encoding
    elif choose == '3':
    
        alg = ChooseMode(['0', '1', '99'], alg_menu)
        
        if alg == '99':
            return
        
        print(base64_file_help)
        
        binary, path = OpenBin()
        
        if alg == '0':
        
            try:
                encode = MirrorEnc(binary).Base64('enc')
                open(path, 'wb').write(encode)
                print("\nEncoded! [{}]".format(path))
            except:
                print("\nNot Encoded! [{}]".format(path))
                
        elif alg == '1':
        
            try:
                decode = MirrorEnc(binary).Base64('dec')
                open(path, 'wb').write(decode)
                print("\nDecoded! [{}]".format(path))
            except:
                print("\nNot Decoded! [{}]".format(path))
            
    # Exit mirror-enc       
    elif choose == '99':
        return
