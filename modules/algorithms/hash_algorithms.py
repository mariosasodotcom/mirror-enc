#!/usr/bin/env python
# -*- coding: utf-8 -*-


import hashlib


def hash_md5(string):
    md5 = hashlib.md5(string).hexdigest()
    return md5


def hash_sha1(string):
    sha1 = hashlib.sha1(string).hexdigest()
    return sha1


def hash_sha224(string):
    sha224 = hashlib.sha224(string).hexdigest()
    return sha224


def hash_sha256(string):
    sha256 = hashlib.sha256(string).hexdigest()
    return sha256
