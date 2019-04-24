#!/usr/bin/env python
# -*- coding: utf-8 -*-


import algorithms.chat_server as chat_server
import algorithms.chat_client as chat_client


def menu():
    menu_chat = """
    [0.] Server   [ Wait an incoming connection ]
    [1.] Client   [ Start an encrypted chat ]   
    [CTRL + C] EXIT mirror-enc  
    """
    print(menu_chat)
    x = ''
    while x not in ['0', '1']:
        x = str(raw_input("mirror-enc > "))
    return x


def main():
    choose = menu()
    if choose == '0':
        chat_server.main()
    elif choose == '1':
        chat_client.main()
