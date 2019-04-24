#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string
import random

from Crypto.PublicKey import RSA


def aes_gen(n):
    chars = string.letters + string.digits + string.punctuation
    key = "".join([random.choice(chars) for x in xrange(n)])
    return key


def rsa_gen(n):
    key = RSA.generate(n)
    f = open("pubKey.pem", 'wb')
    f.write(key.publickey().exportKey('PEM'))
    f.close
    f = open("prvKey.pem", 'wb')
    f.write(key.exportKey('PEM'))
    f.close
