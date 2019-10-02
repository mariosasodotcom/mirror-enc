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
import base64, hashlib, ast, string, random

# From-import statements
from socket import *
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA

# Import mirror-enc modules
from MirrorUtils import *


class MirrorEnc:
    """ Class that contains encryption methods """
    
    def __init__(self, string):
        self.string = string
        
    def RsaEnc(self, key):
    
        prv_key = RSA.importKey(key)
        cipher = prv_key.encrypt(self.string, 32)
        
        return cipher
        
    def RsaDec(self, key):
    
        pub_key = RSA.importKey(key)
        plain = pub_key.decrypt(ast.literal_eval(str(self.string)))
    
        return plain
             
    def RsaGen(self, n):
    
        key = RSA.generate(n)
        prvKey = key.exportKey()
        pubKey = key.publickey().exportKey()
    
        return prvKey, pubKey
        
    def AesEnc(self, key):
    
        null_str = b'\0' * (AES.block_size - len(self.string) % AES.block_size)
        plaintext = self.string + null_str
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)

        return iv + cipher.encrypt(plaintext)
        
    def AesDec(self, key):
    
        iv = self.string[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(self.string[AES.block_size:])
    
        return plaintext.rstrip(b'\0')
        
    def AesGen(self, n): 

        chars = string.letters + string.digits + string.punctuation
        key = "".join([random.choice(chars) for x in xrange(n)])
        
        return key
        
    def Base64(self, alg):

        if alg == 'enc':          
            return base64.b64encode(self.string)

        elif alg == 'dec':          
            return base64.b64decode(self.string)
        
    def GetHashes(self):
       
        hashes = []
       
        hashes.append(hashlib.md5(self.string).hexdigest())
        hashes.append(hashlib.sha1(self.string).hexdigest())
        hashes.append(hashlib.sha224(self.string).hexdigest())
        hashes.append(hashlib.sha256(self.string).hexdigest())
       
        return hashes
