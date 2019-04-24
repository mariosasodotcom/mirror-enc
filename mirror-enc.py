#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import modules.module_chat as module_chat
import modules.module_file as module_file
import modules.module_text as module_text
import modules.module_gen as module_gen


def banner():
    banner_mirror = """

     ___________ @ @                                                     
    /          @\   @                       _                            
    \___________/  _@              ___ __ _(_)__ _ __ _  ___ __ _        
              @  _/@ \_____       / _ ' _` | |__` |__` |/ _ \__` |       
               @/ \__/-=-=^`     | | | | | | |  | |  | | (_) | | |       
                \_ /             |_| |_| |_|_|  |_|  |_|\___/  |_|-enc   
                 <|                                                      
                 <|                    github.com/M4R1OS4S0              
                 <|

    """
    print(banner_mirror)


def initial():
    menu = """
    [0.] CHAT Mode  [ Simple encrypted chat on LAN that combines RSA and AES ]
    [1.] TEXT Mode  [ RSA, AES, Hash and Base64 for texts ]  
    [2.] FILE Mode  [ AES, Hash and Base64 for files ]
    [3.] GEN Mode   [ RSA keypair and AES random key generator ]   
    [CTRL + C] EXIT mirror-enc  
    """
    print(menu)
    x = ''
    while x not in ['0', '1', '2', '3']:
        x = str(raw_input("mirror-enc > "))
    if x == '0':
        mode = 'c'
    elif x == '1':
        mode = 't'
    elif x == '2':
        mode = 'f'
    elif x == '3':
        mode = 'g'
    return mode


def main():
    banner()
    var = 'N'
    while var.upper() == 'N':
        var = ''
        mode = initial()
        if mode == 'c':
            module_chat.main()
        elif mode == 't':
            module_text.main(mode)
        elif mode == 'f':
            module_file.main(mode)
        elif mode == 'g':
            module_gen.main()
        while var.upper() != 'Y' and var.upper() != 'N':
            var = str(raw_input("\nDo you want to close mirror-enc? (Y/N): "))


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n')
        sys.exit()
