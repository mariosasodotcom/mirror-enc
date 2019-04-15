#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import modules.module_file as module_file
import modules.module_text as module_text
import modules.module_gen as module_gen

def banner():   
    banner = """
    
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
    print(banner)

def initial():
    menu = """
    [1.] TEXT Mode  [ RSA, AES, Hash and Base64 ]  
    [2.] FILE Mode  [ AES, Base64 and Hash ]
    [3.] GEN Mode   [ AES and RSA keypair ]   
    [CTRL + C] EXIT mirror-enc  
    """
    print(menu)
    x = '0'
    while x not in ['1', '2', '3']:
        x = str(raw_input("mirror-enc > "))
    if x == '1':
        mode = 't'
    if x == '2':
        mode = 'f'
    if x == '3':
        mode = 'g'
    return mode

def main():
    banner()
    var = 'N'
    while var.upper() == 'N':
        var = ''
        mode = initial()
        if mode == 'f':
            module_file.main(mode)
        elif mode == 't':
            module_text.main(mode)
        elif mode == 'g':
            module_gen.main(mode)
        while var.upper() != 'Y' and var.upper() != 'N':
            var = str(raw_input("\nDo you want to exit? (Y/N): "))

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n')
        sys.exit()
