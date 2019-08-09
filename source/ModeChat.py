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


from socket import *
from MirrorClass import *
from MirrorUtils import *


# Function that encrypt server
def EncryptServer(conn):

    pub = conn.recv(4096)   
    aes = MirrorEnc('').AesGen(32)
    cipher = MirrorEnc(aes).RsaEnc(pub)
    conn.send(str(cipher))
    
    return aes

# Function that encrypt client
def EncryptClient(client):

    prv, pub = MirrorEnc('').RsaGen(1024)
    client.send(pub)
    cipher = client.recv(4096)
    aes = MirrorEnc(cipher).RsaDec(prv)
    
    return aes

# Start chat mode function
def ChatMain():
    
    choose = ChooseMode(['0', '1', '99'], chat_menu)
    
    # Server Side
    if choose == '0':
    
        ip = py_input('\nServer IP: ')
        port = int(py_input('\nPort: '))
        
        server = socket(AF_INET, SOCK_STREAM)
        server.bind((ip, port))
        server.listen(1)
        
        print('\nWaiting for incoming connection...')
        conn, addr = server.accept()
        name = conn.recv(4096)
        print('\nUser {} ({}) joined the chat'.format(name, addr[0]))

        print('\nEncrypting chat with RSA and AES algorithms')
        aes = EncryptServer(conn)
        
        print('Please digit \"exit()\" as a message if you want to exit')
        print('\nWaiting for a message from client\n')
        
        while 1:
            
            # Receive a message
            client_aes = conn.recv(4096)
            client_msg = MirrorEnc(client_aes).AesDec(aes)
            
            if client_msg == 'exit()':
                conn.send(MirrorEnc(client_msg).AesEnc(aes))
                conn.close()
                return
                
            print("< " + name + " > " + client_msg)
            
            # Send a message                  
            server_msg = py_input("< me > ")
            server_aes = MirrorEnc(server_msg).AesEnc(aes)
            conn.send(server_aes)
    
    # Client Side
    elif choose == '1':
    
        ip = py_input('\nServer IP: ')
        port = int(py_input('\nPort: '))
        
        client = socket(AF_INET, SOCK_STREAM)
        client.connect((ip, port))
        
        name = py_input('\nInsert your name: ')
        client.send(name)

        print('\nEncrypting chat with RSA and AES algorithms')
        aes = EncryptClient(client)

        print('\nPlease digit \"exit()\" if you want to exit\n')
        
        while 1:
            
            # Send a message 
            client_msg = py_input("< me > ")
            client_aes = MirrorEnc(client_msg).AesEnc(aes)
            client.send(client_aes)
            
            # Receive a message   
            server_aes = client.recv(4096)
            server_msg = MirrorEnc(server_aes).AesDec(aes)
            
            if server_msg == 'exit()':
                client.send(MirrorEnc(server_msg).AesEnc(aes))
                client.close()
                return
                
            print("< server > " + server_msg)
    
    # Exit mirror-enc        
    elif choose == '99':
        return
