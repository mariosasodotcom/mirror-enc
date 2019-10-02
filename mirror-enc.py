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

# Python 3 is not supported
if sys.version_info.major == 3:
    print('\nError: mirror-enc do not support python3\n')
    sys.exit()


# Import mirror-enc modules
from mirrorenc.MirrorUtils import *
from mirrorenc.__main__ import main


# Start mirror-enc
if __name__ == '__main__':
    main()
