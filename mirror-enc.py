#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    Copyright (C) 2019-2020 Mario Saso (github.com/M4R1OS4S0)
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

# --------------------------| Meta |--------------------------- #

__version__ = '1.0.0'
__license__ = 'GPLv3'
__author__ = 'Mario Saso'
__email__ = 'mariosaso@protonmail.com'
__url__ = 'https://github.com/M4R1OS4S0/mirror-enc'

# -------------------------| Imports |------------------------- #

# Import statements
import os
import sys
import string
import random
import base64
import hashlib

# PyCrypto imports
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA

# --------------------------| Class |-------------------------- #

class MirrorEnc:
    """ Class that contains mirror-enc methods """
    
    def __init__(self, arg_list):
        # _____________________________________________________________
        # RSA Encrypt & Decrypt   |arg_list = [alg, pubkeypath, string]|
        if (arg_list[0] == '--rsa-enc' or arg_list[0] == '--rsa-dec'):      
            self.alg = arg_list[0]
            self.keypath = arg_list[1]
            self.key = open(arg_list[1], 'rb').read()
            self.string = arg_list[2]
        # _______________________________________________
        # RSA Keypair Gen   |arg_list = [alg, dirkeypath]|
        elif arg_list[0] == '--rsa-gen':
            self.alg = arg_list[0]
            self.dirkeypath = arg_list[1]
        # _________________________________________________________________
        # AES Encrypt & Decrypt   |arg_list = [alg, key, mode, string/path]|
        elif arg_list[0] == '--aes-enc' or arg_list[0] == '--aes-dec':
            self.alg = arg_list[0]
            self.key = hashlib.sha256(arg_list[1]).digest()
            self.mode = arg_list[2]
            if self.mode == 'string':
                self.string = arg_list[3]
            elif self.mode == 'file':
                self.string = open(arg_list[3], 'rb').read()
                self.binpath = arg_list[3]
        # __________________________________________________  
        # Get Hashes    |arg_list = [alg, mode, string/path]|
        elif arg_list[0] == '--get-hashes':
            self.alg = arg_list[0]
            self.mode = arg_list[1]
            if self.mode == 'string':
                self.string = arg_list[2]
            elif self.mode == 'file':
                self.string = open(arg_list[2], 'rb').read()
                self.binpath = arg_list[2]
        
    def rsa_enc(self):
        prv_key = RSA.importKey(self.key)
        cipher = prv_key.encrypt(self.string, 32)
        return cipher[0]
        
    def rsa_dec(self):
        pub_key = RSA.importKey(self.key)
        plain = pub_key.decrypt(self.string)
        return plain
             
    def rsa_gen(self):
        key = RSA.generate(2048)
        prv_key = key.exportKey()
        pub_key = key.publickey().exportKey()
        os.chdir(self.dirkeypath)
        open('prvKey', 'wb').write(prv_key)
        open('pubKey', 'wb').write(pub_key)

    def aes_enc(self):
        null_str = b'\0' * (AES.block_size - len(self.string) % AES.block_size)
        plaintext = self.string + null_str
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        ciphertext = iv + cipher.encrypt(plaintext)
        return ciphertext
        
    def aes_dec(self):
        #not_b64 = base64.b64decode(self.string)
        iv = self.string[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)   
        plaintext = cipher.decrypt(self.string[AES.block_size:])
        return plaintext.rstrip(b'\0')
        
    def get_hashes(self):
        hashes = []
        hashes.append(hashlib.md5(self.string).hexdigest())
        hashes.append(hashlib.sha1(self.string).hexdigest())
        hashes.append(hashlib.sha224(self.string).hexdigest())
        hashes.append(hashlib.sha256(self.string).hexdigest())
        return hashes

# ------------------------| Variables |------------------------ #

# Variable for mirror-enc banner
banner = """
     ___________ @ @                                                     
    /  v1.0.0  @\   @                       _                            
    \___________/  _@              ___ __ _(_)__ _ __ _  ___ __ _        
              @  _/@ \_____       / _ ' _` | |__` |__` |/ _ \__` |       
               @/ \__/-=-=^`     | | | | | | |  | |  | | (_) | | |       
                \_ /             |_| |_| |_|_|  |_|  |_|\___/  |_|-enc   
                 <|                                                      
                 <|               .:   <github.com/M4R1OS4S0>   :.             
                 <|               .: <mariosaso@protonmail.com> :.
"""

# Variable for mirror-enc help
usage = """
    Usage:    
    
    $ python mirror-enc.py --rsa-enc -k <pub_key_path> -s <plaintext_string>
    [RSA String Encryption]
    
    $ python mirror-enc.py --rsa-dec -k <prv_key_path> -s <ciphertext_string>
    [RSA String Decryption]
    
    $ python mirror-enc.py --rsa-gen -d <dir_path>
    [RSA Keypair Generator]
    
    $ python mirror-enc.py --aes-enc -k <key> -s <plaintext_string>
    [AES String Encryption]
    
    $ python mirror-enc.py --aes-dec -k <key> -s <ciphertext_string>
    [AES String Decryption]
    
    $ python mirror-enc.py --aes-enc -k <key> -f <plaintext_file_path>
    [AES File Encryption]
    
    $ python mirror-enc.py --aes-dec -k <key> -f <ciphertext_file_path>
    [AES File Decryption]
    
    $ python mirror-enc.py --get-hashes -s <string>
    [HASH String Calculator]
    
    $ python mirror-enc.py --get-hashes -f <file_path>
    [HASH File Calculator]
"""

# Variable for rsa enc/dec help    
rsa_encdec_help = """
    This module uses Rivest Shamir Adleman (RSA) to encrypt and decrypt
    strings. A public key is used to encrypt strings and a private key 
    is used to decrypt strings. Encrypted chipertext will be (or must be,
    if as input) encoded with Base64.  """
    
# Variable for rsa generator help
rsa_gen_help = """
    This module generates RSA keypairs (public and private keys)
    that will be saved in a directory. """
    
# Variable for aes string help    
aes_string_help = """
    This module uses Advanced Encryption Standard (AES) to encrypt and
    decrypt strings. Encrypted chipertext will be (or must be, if as input)
    encoded with Base64. The key which is used to encrypt should be the
    same as the key that will be used for decrypt. """
    
# Variable for aes file help
aes_file_help = """
    This module uses Advanced Encryption Standard (AES) to encrypt and
    decrypt files. The key which is used to encrypt should be the same 
    as the key that will be used for decrypt. """
    
# Variable for hash help   
hashes_help = """
    This module uses MD5, SHA-1, SHA-224 and SHA-256 algorithms to 
    generate hashes. Hashing is a method of taking data, encrypting
    it, and creating unpredictable, irreversible output. """

# ------------------------| Functions |------------------------ #

def get_arg_list(argv):
    
    # RSA String Enc
    if (len(argv) == 6 and
        argv[1] == '--rsa-enc' and
        argv[2] == '-k' and
        argv[4] == '-s'):
        return [argv[1], argv[3], argv[5]]
    
    # RSA String Dec
    elif (len(argv) == 6 and
        argv[1] == '--rsa-dec' and
        argv[2] == '-k' and
        argv[4] == '-s'):
        return [argv[1], argv[3], argv[5]]
    
    # RSA Key Gen
    elif (len(argv) == 4 and
        argv[1] == '--rsa-gen' and
        argv[2] == '-d'):
        return [argv[1], argv[3]]
        
    # AES String Enc
    elif (len(argv) == 6 and
        argv[1] == '--aes-enc' and
        argv[2] == '-k' and
        argv[4] == '-s'):
        return [argv[1], argv[3], 'string', argv[5]]
        
    # AES String Dec
    elif (len(argv) == 6 and
        argv[1] == '--aes-dec' and
        argv[2] == '-k' and
        argv[4] == '-s'):
        return [argv[1], argv[3], 'string', argv[5]]
        
    # AES File Enc
    elif (len(argv) == 6 and
        argv[1] == '--aes-enc' and
        argv[2] == '-k' and
        argv[4] == '-f'):
        return [argv[1], argv[3], 'file', argv[5]]
        
    # AES File Dec
    elif (len(argv) == 6 and
        argv[1] == '--aes-dec' and
        argv[2] == '-k' and
        argv[4] == '-f'):
        return [argv[1], argv[3], 'file', argv[5]]
        
    # Get String Hashes
    elif (len(argv) == 4 and
        argv[1] == '--get-hashes' and
        argv[2] == '-s'):
        return [argv[1], 'string', argv[3]]
        
    # Get File Hashes
    elif (len(argv) == 4 and
        argv[1] == '--get-hashes' and
        argv[2] == '-f'):
        return [argv[1], 'file', argv[3]]
        
    # Help
    else:
        print(usage)
        sys.exit()         

def run(arg_list):
    
    # Mirror-enc object
    obj = MirrorEnc(arg_list)
    
    # RSA Encryption
    if (obj.alg == '--rsa-enc'):
        print(rsa_encdec_help)
        print('\nPlaintext: ' + obj.string)
        print('\nPubkey path: ' + obj.keypath)
        print('\nEncrypting string (RSA)...')
        cipher = obj.rsa_enc()
        encoded = base64.b64encode(str(cipher))
        print('\n[+] Ciphertext: ' + encoded + '\n')

    # RSA Decryption
    elif (obj.alg == '--rsa-dec'):
        print(rsa_encdec_help)
        print('\nCiphertext: ' + obj.string)
        print('\nPrvkey path: ' + obj.keypath)
        print('\nDecrypting string (RSA)...')
        obj.string = base64.b64decode(obj.string)
        plain = obj.rsa_dec()
        print('\n[+] Plaintext: ' + str(plain) + '\n')

    # RSA Keypair Gen
    elif (obj.alg == '--rsa-gen'):
        print(rsa_gen_help)
        print('\nKeypair folder: ' + obj.dirkeypath)
        print('\nGenerating keypair RSA-2048...')
        obj.rsa_gen()
        print('\n[+] Done!' + '\n')

    # AES Encryption
    elif (obj.alg == '--aes-enc'):
        if (obj.mode == 'string'):
            print(aes_string_help)
            print('\nString: ' + obj.string)
            print('\nEncrypting string (AES-256)...')
            cipher = obj.aes_enc()
            encoded = base64.b64encode(str(cipher))
            print('\n[+] Ciphertext: ' + encoded + '\n')
        elif (obj.mode == 'file'):
            print(aes_file_help)
            print('\nFile: ' + obj.binpath)
            print('\nEncrypting file (AES-256)...')
            cipher = obj.aes_enc()
            open(obj.binpath, 'wb').write(cipher)
            print('\n[+] Done!' + '\n')

    # AES Decryption
    elif (obj.alg == '--aes-dec'):
        if (obj.mode == 'string'):
            print(aes_string_help)
            print('\nString: ' + obj.string)
            print('\nDecrypting string (AES-256)...')
            obj.string = base64.b64decode(obj.string)
            plain = obj.aes_dec()
            print('\n[+] Plaintext: ' + str(plain) + '\n')
        elif (obj.mode == 'file'):
            print(aes_file_help)
            print('\nFile: ' + obj.binpath)
            print('\nDecrypting file (AES-256)...')
            plain = obj.aes_dec()
            open(obj.binpath, 'wb').write(plain)
            print('\n[+] Done!' + '\n')

    # Get Hashes
    elif (obj.alg == '--get-hashes'):
        print(hashes_help)
        if (obj.mode == 'string'):
            print('\nString: ' + obj.string)
        elif (obj.mode == 'file'):
            print('\nFile: ' + obj.binpath)
        print('\nCalculating hashes...')
        hashes = obj.get_hashes()
        print('')
        print('[+] MD5:\t' + str(hashes[0]))
        print('[+] SHA-1:\t' + str(hashes[1]))
        print('[+] SHA-224:\t' + str(hashes[2]))
        print('[+] SHA-256:\t' + str(hashes[3]))
        print('')
        
def main():
    
    # Py version info controller
    if sys.version_info.major == 3:
        print('\nError: mirror-enc do not support python3\n')
        sys.exit()
    
    # Print mirror-enc banner
    print(banner)
    
    # Get arguments
    arg_list = get_arg_list(sys.argv)
    
    # Start mirror-enc
    try:
        run(arg_list)
    except:
        print('\n[-] An error has occurred' + '\n')

if __name__ == '__main__':
    main()
