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


# Start generator mode function
def GenMain():

    choose = ChooseMode(['0', '1', '2', '3', '4', '5', '99'], gen_menu)
    
    if choose == '99':
        return
    
    print(gen_help)
    
    # RSA-1024 Keypair
    if choose == '0':
    
        directory = OpenDir()
        os.chdir(directory)
        
        prv, pub = MirrorEnc('').RsaGen(1024)
        open('prvKey', 'wb').write(prv)
        open('pubKey', 'wb').write(pub)
        
        print("\nRSA-1024 Keypair generated!")
    
    # RSA-2048 Keypair
    elif choose == '1':
    
        directory = OpenDir()
        os.chdir(directory)
        
        prv, pub = MirrorEnc('').RsaGen(2048)
        open('prvKey', 'wb').write(prv)
        open('pubKey', 'wb').write(pub)
        
        print("\nRSA-2048 Keypair generated!")
    
    # RSA-4096 Keypair
    elif choose == '2':
    
        directory = OpenDir()
        os.chdir(directory)
        
        prv, pub = MirrorEnc('').RsaGen(4096)
        open('prvKey', 'wb').write(prv)
        open('pubKey', 'wb').write(pub)
        
        print("\nRSA-4096 Keypair generated!")
    
    # AES-128 Random Key
    elif choose == '3':
    
        key = MirrorEnc('').AesGen(16)
        print("\nAES-128 Key: {}".format(key))
    
    # AES-192 Random Key
    elif choose == '4':
    
        key = MirrorEnc('').AesGen(24)
        print("\nAES-192 Key: {}".format(key))
    
    # AES-256 Random Key    
    elif choose == '5':
    
        key = MirrorEnc('').AesGen(32)
        print("\nAES-256 Key: {}".format(key))
