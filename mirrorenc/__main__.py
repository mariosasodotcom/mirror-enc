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
import sys

# Import mirror-enc modules
import ModeChat, ModeGen
import ModeStr, ModeFile
from MirrorUtils import *


# Start main function
def start():

    print(banner_mirror)
    
    var = 'N'
    while var.upper() == 'N':
    
        var = ''
        mode = ChooseMode(['0', '1', '2', '3', '99'], init_menu)
        
        # Chat Mode
        if mode == '0':
            ModeChat.ChatMain()
        
        # File Mode    
        elif mode == '1':
            ModeFile.FileMain()
        
        # String Mode             
        elif mode == '2':
            ModeStr.StrMain()
        
        # Generator Mode    
        elif mode == '3':
            ModeGen.GenMain()           
            
        while var.upper() != 'Y' and var.upper() != 'N':
            var = py_input("\nDo you want to close mirror-enc? (Y/N): ")


# Start mirror-enc
def main():

    try:
        ClearScreen()
        start()
        ClearScreen()
        
    except KeyboardInterrupt:
        ClearScreen()
