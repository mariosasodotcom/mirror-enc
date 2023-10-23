#!/usr/bin/env python3
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
                 <|               .:   <github.com/M4R1OS4S0>    :.             
                 <|               .: <mariosaso@protonmail.com>  :.
                                  .: <https://www.mariosaso.com> :.
                                  
            A GPG Frontend that uses AES & RSA algorithms.
									
"""
menu = """
                  .:: Symmetric Encryption ::.
					
This module uses Advanced Encryption Standard (AES) to encrypt and
decrypt files. The key which is used to encrypt should be the
same as the key that will be used for decrypt.
					
1. AES-256 File Enc              2. AES-256 File Dec



                  .:: Asymmetric Encryption ::.
					
This module uses Rivest Shamir Adleman (RSA) to generate keypairs and 
encrypt and decrypt files. Public key is used to encrypt and private key 
is used to decrypt.
    
3. Generate Keypair              4. Generate Default Keypair

5. Import Local Key              6. Export Local Key

7. Show Public Keys              8. Show Private Keys

9. Delete Public Key            10. Delete Private Key

11. Encrypt File (PublicKey)    12. Decrypt File (PrivateKey)



                      .:: Fingerprint ::.
					  	
This module uses MD5, SHA-1, SHA-224 and SHA-256 algorithms to 
generate hashes. Hashing is a method of taking data, encrypting
it, and creating unpredictable, irreversible output.
    
13. MD5 Hash                    14. SHA-1 Hash

15. SHA-224 Hash                16. SHA-256 Hash



                         .:: Other ::.
                        
This module shows menu or exit from mirror-enc tool.
                        
0. Menu mirror-enc              00. Exit mirror-enc


"""

# -------------------------| Imports |------------------------- #

# Import statements
import sys
import subprocess

# ------------------------| Functions |------------------------ #

def set_option(opts):
	option = input('Choose a number > ')
	while option not in opts:
		option = input('Choose a number > ')
	print()
	return option
	
def normalize(string):	
	""" Function that prevent a drag&drop bug """         

	if (string[0] == '\''):
		return string.split('\'')[1] 

	elif (string[0] == '\"'):
		return string.split('\"')[1] 

	return string
	
def clear_screen():
	subprocess.run(['clear'])
	
# ------------------------| Modules |-------------------------- #

def aes_enc(file):
	command = ["gpg", "-a", "-o", file+".aes", "--symmetric", "--cipher-algo", "AES256", file]
	out = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	if (out.returncode == 0):
		print("\n[+] File is correctly encrypted")
		print(out.stdout.decode('utf-8'))
	else:
		print("\n[-] An error has occurred")
		print(out.stderr.decode('utf-8'))
	
def aes_dec(file):
	command = ["gpg", "-o", file[:-4], "-d", file]
	out = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	if (out.returncode == 0):
		print("\n[+] File is correctly decrypted")
		print(out.stdout.decode('utf-8'))
	else:
		print("\n[-] An error has occurred")
		print(out.stderr.decode('utf-8'))
		
def rsa_gen():
	command = ["gpg", "--full-generate-key"]
	out = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	if (out.returncode == 0):
		print("\n[+] Keypair is correctly generated")
		print(out.stdout.decode('utf-8'))
	else:
		print("\n[-] An error has occurred")
		print(out.stderr.decode('utf-8'))
		
def rsa_def_gen():
	command = ["gpg", "--gen-key"]
	out = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	if (out.returncode == 0):
		print("\n[+] Keypair is correctly generated")
		print(out.stdout.decode('utf-8'))
	else:
		print("\n[-] An error has occurred")
		print(out.stderr.decode('utf-8'))
		
def rsa_import(file):
	command = ["gpg", "--import", file]
	out = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	if (out.returncode == 0):
		print("\n[+] Key is correctly imported")
		print(out.stdout.decode('utf-8'))
	else:
		print("\n[-] An error has occurred")
		print(out.stderr.decode('utf-8'))

def rsa_export(uid):
	command = ["gpg", "--export", uid]
	out = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	if (out.returncode == 0):
		print("\n[+] Key is correctly exported")
		print(out.stdout.decode('utf-8'))
	else:
		print("\n[-] An error has occurred")
		print(out.stderr.decode('utf-8'))
		
def rsa_list():
	command = ["gpg", "--list-keys"]
	out = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	if (out.returncode == 0):
		print("\n[+] Public Keys are correctly loaded")
		print(out.stdout.decode('utf-8'))
	else:
		print("\n[-] An error has occurred")
		print(out.stderr.decode('utf-8'))
		
def rsa_sec_list():
	command = ["gpg", "--list-secret-keys"]
	out = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	if (out.returncode == 0):
		print("\n[+] Private Keys are correctly loaded")
		print(out.stdout.decode('utf-8'))
	else:
		print("\n[-] An error has occurred")
		print(out.stderr.decode('utf-8'))
		
def rsa_delete(uid):
	command = ["gpg", "--delete-key", uid]
	out = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	if (out.returncode == 0):
		print("\n[+] Key is correctly deleted")
		print(out.stdout.decode('utf-8'))
	else:
		print("\n[-] An error has occurred")
		print(out.stderr.decode('utf-8'))

def rsa_sec_delete(uid):
	command = ["gpg", "--delete-secret-key", uid]
	out = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	if (out.returncode == 0):
		print("\n[+] Key is correctly deleted")
		print(out.stdout.decode('utf-8'))
	else:
		print("\n[-] An error has occurred")
		print(out.stderr.decode('utf-8'))
		
def rsa_enc(uid_pub, file):
	command = ["gpg", "-o", file+".rsa", "-r", uid_pub, "--armor", "--encrypt", file]
	out = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	if (out.returncode == 0):
		print("\n[+] File is correctly encrypted")
		print(out.stdout.decode('utf-8'))
	else:
		print("\n[-] An error has occurred")
		print(out.stderr.decode('utf-8'))
		
def rsa_dec(uid_prv, file):
	command = ["gpg", "-o", file[:-4], "-u", uid_prv, "-d", file]
	out = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	if (out.returncode == 0):
		print("\n[+] File is correctly decrypted")
		print(out.stdout.decode('utf-8'))
	else:
		print("\n[-] An error has occurred")
		print(out.stderr.decode('utf-8'))
		
def md5(file):
	command = ["md5sum", file]
	out = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	if (out.returncode == 0):
		print("\n[+] MD5 is correctly calculated")
		print(out.stdout.decode('utf-8'))
	else:
		print("\n[-] An error has occurred")
		print(out.stderr.decode('utf-8'))
		
def sha1(file):
	command = ["sha1sum", file]
	out = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	if (out.returncode == 0):
		print("\n[+] SHA-1 is correctly calculated")
		print(out.stdout.decode('utf-8'))
	else:
		print("\n[-] An error has occurred")
		print(out.stderr.decode('utf-8'))
		
def sha224(file):
	command = ["sha224sum", file]
	out = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	if (out.returncode == 0):
		print("\n[+] SHA-224 is correctly calculated")
		print(out.stdout.decode('utf-8'))
	else:
		print("\n[-] An error has occurred")
		print(out.stderr.decode('utf-8'))
		
def sha256(file):
	command = ["sha256sum", file]
	out = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	if (out.returncode == 0):
		print("\n[+] SHA-256 is correctly calculated")
		print(out.stdout.decode('utf-8'))
	else:
		print("\n[-] An error has occurred")
		print(out.stderr.decode('utf-8'))
		
# ---------------------------| Main |-------------------------- #

def start():
	
	opts = ['00', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
	option = set_option(opts)
	
	if (option == '1'):
		file_in = input('File path: ')
		file = normalize(file_in)
		aes_enc(file)
		
	elif (option == '2'):
		file_in = input('File path: ')
		file = normalize(file_in)
		aes_dec(file)
		
	elif (option == '3'):
		rsa_gen()
		
	elif (option == '4'):
		rsa_def_gen()
		
	elif (option == '5'):
		file_in = input('Key path: ')
		file = normalize(file_in)
		rsa_import(file)
		
	elif (option == '6'):
		uid = input('UID: ')
		rsa_export(uid)
		
	elif (option == '7'):
		rsa_list()
		
	elif (option == '8'):
		rsa_sec_list()
		
	elif (option == '9'):
		uid = input('Public UID: ')
		rsa_delete(uid)
		
	elif (option == '10'):
		uid = input('Private UID: ')
		rsa_sec_delete(uid)
		
	elif (option == '11'):
		uid = input('Recipient Public UID: ')
		file_in = input('File path: ')
		file = normalize(file_in)
		rsa_enc(uid, file)
		
	elif (option == '12'):
		uid = input('Private UID: ')
		file_in = input('File path: ')
		file = normalize(file_in)
		rsa_dec(uid, file)
		
	elif (option == '13'):
		file_in = input('File path: ')
		file = normalize(file_in)
		md5(file)
		
	elif (option == '14'):
		file_in = input('File path: ')
		file = normalize(file_in)
		sha1(file)
		
	elif (option == '15'):
		file_in = input('File path: ')
		file = normalize(file_in)
		sha224(file)
		
	elif (option == '16'):
		file_in = input('File path: ')
		file = normalize(file_in)
		sha256(file)
		
	elif (option == '0'):
		print(menu)
		
	elif (option == '00'):
		sys.exit(0)

def run():
    while 1:
        try:
            start()
        except KeyboardInterrupt:
            print('\n')
            run()

def main():
    clear_screen()
    print(banner)
    print(menu)
    run()
    
if __name__ == '__main__':
	main()
