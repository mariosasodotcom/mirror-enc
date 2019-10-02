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


# Import mirror-enc modules
from MirrorClass import *
from MirrorUtils import *


# Start string mode function
def StrMain():

    choose = ChooseMode(['0', '1', '2', '3', '99'], string_menu)
    
    # RSA Encryption
    if choose == '0':
    
        alg = ChooseMode(['0', '1', '99'], alg_menu)
        
        if alg == '99':
            return
        
        print(rsa_string_help)
        
        key = RsaChooseKey(alg)
        string = py_input("\nString: ")
        
        if alg == '0':
        
            try:
                cipher = MirrorEnc(string).RsaEnc(key)
                print("\nCiphertext: {}".format(str(cipher)))
            except:
                print("\nNot Encrypted!")
                
        elif alg == '1':
        
            try:
                plain = MirrorEnc(string).RsaDec(key)
                print("\nPlaintext: {}".format(str(plain)))
            except:
                print("\nNot Decrypted!")
    
    # AES Encryption
    elif choose == '1':
    
        alg = ChooseMode(['0', '1', '99'], alg_menu)
        
        if alg == '99':
            return
        
        print(aes_string_help)
        
        key = AesChooseKey()
        string = py_input("\nString: ")
        
        if alg == '0':
        
            try:
                cipher = MirrorEnc(string).AesEnc(key)
                b64_cipher = MirrorEnc(cipher).Base64('enc')
                print("\nCiphertext: {}".format(b64_cipher))
            except:
                print("\nNot Encrypted!")
                
        elif alg == '1':
        
            try:
                cipher = MirrorEnc(string).Base64('dec')
                plain = MirrorEnc(cipher).AesDec(key)
                print("\nPlaintext: {}".format(plain))
            except:
                print("\nNot Decrypted!")
    
    # Hash Algorithms
    elif choose == '2':
    
        print(hash_string_help)
        string = py_input("\nString: ")
        
        hashes = MirrorEnc(string).GetHashes()
        
        print("\nMD5: " + hashes[0])
        print("SHA-1: " + hashes[1])
        print("SHA-224: " + hashes[2])
        print("SHA-256: " + hashes[3])
    
    # Base64 Encoding
    elif choose == '3':
    
        alg = ChooseMode(['0', '1', '99'], alg_menu)
        
        if alg == '99':
            return
        
        print(base64_string_help)
        
        string = py_input("\nString: ")
        
        if alg == '0':
        
            try:
                encode = MirrorEnc(string).Base64('enc')
                print("\nCiphertext: {}".format(encode))
            except:
                print("\nNot Encoded!")
                
        elif alg == '1':
        
            try:
                decode = MirrorEnc(string).Base64('dec')
                print("\nPlaintext: {}".format(decode))
            except:
                print("\nNot Decoded!")
            
    # Exit mirror-enc       
    elif choose == '99':
        return
