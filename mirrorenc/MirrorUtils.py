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
import sys, subprocess, os, platform


# Input function for Python 2 & 3
def py_input(string):

    if sys.version_info.major == 2:
        return str(raw_input(string))
        
    elif sys.version_info.major == 3:
        return str(input(string))
               
# Closs platform screen cleaner
def ClearScreen():

    if platform.system() == 'Linux':
        subprocess.call('clear', shell=True)
        
    elif platform.system() == 'Windows':
        subprocess.call('cls', shell=True)

# Function that prevent a drag&drop bug          
def StrNormalize(string):

    if string[0] == '\'':
        return string.split('\'')[1] 
               
    elif string[0] == '\"':
        return string.split('\"')[1] 
        
    return string
            
# Function that choose options
def ChooseMode(n_list, banner):

    print(banner)
    choise = py_input("mirror-enc > ")
    
    while choise not in n_list:
        choise = py_input("mirror-enc > ")
        
    return choise

# Function that choose rsa key   
def RsaChooseKey(alg):

    if alg == '0':
        key_path = StrNormalize(py_input("\npubKey path: "))
        
    elif alg == '1':
        key_path = StrNormalize(py_input("\nprvKey path: "))
        
    if os.path.isfile(key_path):
        key = open(key_path, 'rb').read()    
        return key
        
    print("This is not a file or it does not exist")
    RsaChooseKey(alg)

# Function that choose aes key    
def AesChooseKey():

    key = py_input("\nAES key encryption (128, 192 or 256 bits): ")
    valid_size = [16, 24, 32]
    
    if len(key) in valid_size:
        return key
        
    print("Error! Your key must be 16, 24 or 32 bytes long")
    AesChooseKey()
    
# Function that choose dir path   
def OpenDir():

    path = StrNormalize(py_input("\nDirectory path: "))
    
    if os.path.isdir(path):
        return path
        
    print("This is not a directory or it does not exist")
    OpenDir()
 
# Function that choose file path   
def OpenBin():

    path = StrNormalize(py_input("\nFile path: "))
    
    if os.path.isfile(path):
        binary = open(path, 'rb').read()
        return binary, path
        
    print("This is not a file or it does not exist")
    OpenBin()

# Variable for mirror-enc banner
banner_mirror = """
     ___________ @ @                                                     
    /  v0.0.1  @\   @                       _                            
    \___________/  _@              ___ __ _(_)__ _ __ _  ___ __ _        
              @  _/@ \_____       / _ ' _` | |__` |__` |/ _ \__` |       
               @/ \__/-=-=^`     | | | | | | |  | |  | | (_) | | |       
                \_ /             |_| |_| |_|_|  |_|  |_|\___/  |_|-enc   
                 <|                                                      
                 <|               .:   <github.com/M4R1OS4S0>   :.             
                 <|               .: <mariosaso@protonmail.com> :.
"""

# Variable for mirror-enc menu
init_menu = """
    [0.]  CHAT Mode         [   Combining RSA and AES for enc chat     ]
    [1.]  FILE Mode         [     AES, Hash and Base64 for files       ]
    [2.]  STRING Mode       [  RSA, AES, Hash and Base64 for strings   ]  
    [3.]  GENERATOR Mode    [ RSA keypair and AES random key generator ]   
    [99.] EXIT mirror-enc   
    """
  
# Variable for chat mode menu
chat_menu = """
    [0.] Server Side        [ Wait an incoming connection ]
    [1.] Client Side        [   Start an encrypted chat   ]   
    [99.] EXIT mirror-enc     
    """

# Variable for string mode menu
string_menu = """
    [0.]  RSA Encryption    [ RSA-1024, RSA-2048, RSA-4096 ]
    [1.]  AES Encryption    [   AES-128, AES-192, AES-256  ]
    [2.]  HASH Algorithms   [ MD5, SHA-1, SHA-224, SHA-256 ]
    [3.]  BASE64 Encoding   [      STRING <=> BASE64       ]
    [99.] EXIT mirror-enc      
    """
    
# Variable for file mode menu
file_menu = """
    [0.] RSA Encryption     [   Not available in file mode    ]
    [1.] AES Encryption     [    AES-128, AES-192, AES-256    ]
    [2.] HASH Algorithms    [  MD5, SHA-1, SHA-224, SHA-256   ]
    [3.] BASE64 Encoding    [         FILE <=> BASE64         ]
    [99.] EXIT mirror-enc      
    """

# Variable for gen mode menu
gen_menu = """
    [0.] Generate RSA-1024 Keypair
    [1.] Generate RSA-2048 Keypair
    [2.] Generate RSA-4096 Keypair
    [3.] Generate AES-128 Random Key
    [4.] Generate AES-192 Random Key
    [5.] Generate AES-256 Random Key
    [99.] EXIT mirror-enc  
    """
    
# Variable for algorithms menu
alg_menu = """
    [0.] From plaintext to ciphertext
    [1.] From ciphertext to plaintext
    [99.] EXIT mirror-enc  
    """

# Variable for aes file help
aes_file_help = """
    This module uses Advanced Encryption Standard (AES) to encrypt and
    decrypt files. The key which is used to encrypt should be the same 
    as the key that will be used for decrypt. Change the AES key lenght 
    either 16, 24 or 32 bytes to select AES-128, AES-192 or AES-256. """

# Variable for hash file help   
hash_file_help = """
    This module uses MD5, SHA-1, SHA-224 and SHA-256 algorithms to 
    generate file hashes. Hashing is a method of taking data, encrypting
    it, and creating unpredictable, irreversible output. """

# Variable for base64 file help    
base64_file_help = """
    This module uses Base64 algorithm to encode or decode files.
    Base64 is encoding that allows files or data to be embedded in 
    media that otherwise does not allow certain data. """

# Variable for rsa string help    
rsa_string_help = """
    This module uses Rivest Shamir Adleman (RSA) to encrypt and decrypt
    strings. A Public Key is used to encrypt strings and a Private Key 
    is used to decrypt strings. """

# Variable for aes string help    
aes_string_help = """
    This module uses Advanced Encryption Standard (AES) to encrypt and
    decrypt strings. Encrypted chipertext will be (or must be, if as input)
    encoded with Base64. The key which is used to encrypt should be the
    same as the key that will be used for decrypt. Change the AES key lenght
    either 16, 24 or 32 bytes to select AES-128, AES-192 or AES-256. """

# Variable for hash string help   
hash_string_help = """
    This module uses MD5, SHA-1, SHA-224 and SHA-256 algorithms to 
    generate syting hashes. Hashing is a method of taking data, encrypting
    it, and creating unpredictable, irreversible output. """

# Variable for base64 string help   
base64_string_help = """
    This module uses Base64 algorithm to encode or decode strings.
    Base64 is encoding that allows files or data to be embedded in 
    media that otherwise does not allow certain data. """
    
# Variable for generator help
gen_help = """
    This module generates random AES keys and RSA keypairs.
    RSA keypairs will be saved in a directory, AES keys will
    be shown in terminal. """
