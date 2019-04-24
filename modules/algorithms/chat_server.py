#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import tempfile
from socket import *

from Crypto.PublicKey import RSA

import aes_encryption
import rsa_encryption
from key_gen import *


def encrypt_server(conn):
    temp = tempfile.gettempdir()
    os.chdir(temp)
    pub = conn.recv(4096)
    f = open("pubKey1.pem", 'wb')
    f.write(pub)
    f.close()
    f = open("pubKey1.pem", 'rb')
    pub = RSA.importKey(f.read())
    f.close()
    os.remove("pubKey1.pem")
    aes = aes_gen(32)
    cipher = rsa_encryption.encrypt(aes, pub)
    conn.send(str(cipher))
    return aes


def recv(aes, conn, name):
    client_aes = conn.recv(4096)
    client_ = aes_encryption.decrypt(client_aes, aes)
    if client_ == "exit()":
        conn.send(aes_encryption.encrypt("exit()", aes))
        conn.close()
        sys.exit()
    print("< " + name + " > " + client_)


def send(aes, conn):
    server_ = raw_input("< me > ")
    server_aes = aes_encryption.encrypt(server_, aes)
    conn.send(server_aes)


def main():
    ip = str(raw_input("\nServer IP: "))
    port = int(raw_input("\nPort: "))
    server = socket(AF_INET, SOCK_STREAM)
    server.bind((ip, port))
    server.listen(1)
    print("\nWaiting for incoming connection...")
    conn, addr = server.accept()
    name = conn.recv(4096)
    join = '\nUser ' + name + " (" + addr[0] + ") joined the chat"
    print(join)

    print("\nEncrypting chat with RSA and AES algorithms")
    aes = encrypt_server(conn)

    print("\nWaiting for a message from client\n")
    while 1:
        recv(aes, conn, name)
        send(aes, conn)
