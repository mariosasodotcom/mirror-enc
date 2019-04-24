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


def encrypt_client(client):
    temp = tempfile.gettempdir()
    os.chdir(temp)
    rsa_gen(1024)
    f = open("pubKey.pem", 'rb')
    pub = f.read()
    f.close()
    f = open("prvKey.pem", 'rb')
    prv = RSA.importKey(f.read())
    f.close()
    os.remove("pubKey.pem")
    os.remove("prvKey.pem")
    client.send(str(pub))
    cipher = client.recv(4096)
    aes = rsa_encryption.decrypt(cipher, prv)
    return aes


def send(aes, client):
    client_ = raw_input("< me > ")
    client_aes = aes_encryption.encrypt(client_, aes)
    client.send(client_aes)


def recv(aes, client):
    server_aes = client.recv(4096)
    server_ = aes_encryption.decrypt(server_aes, aes)
    if server_ == "exit()":
        client.send(aes_encryption.encrypt("exit()", aes))
        client.close()
        sys.exit()
    print("< server > " + server_)


def main():
    ip = str(raw_input("\nServer IP: "))
    port = int(raw_input("\nPort: "))
    client = socket(AF_INET, SOCK_STREAM)
    client.connect((ip, port))
    name = raw_input("\nInsert your name: ")
    client.send(name)

    print("\nEncrypting chat with RSA and AES algorithms")
    aes = encrypt_client(client)

    print("\nPlease digit \"exit()\" if you want to exit\n")
    while 1:
        send(aes, client)
        recv(aes, client)
