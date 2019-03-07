#!/usr/bin/env python


import os
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



def hash_list(files):

    for file in files:

        print("\nFile: " + os.path.abspath(file))

        try:

            with open(file, 'rb') as fopen:
                bin_file = fopen.read()

            md5 = hash_md5(bin_file)
            sha1 = hash_sha1(bin_file)
            sha224 = hash_sha224(bin_file)
            sha256 = hash_sha256(bin_file)

            print("MD5: " + md5)
            print("SHA-1: " + sha1)
            print("SHA-224: " + sha224)
            print("SHA-256: " + sha256)

        except:
            print("Error")


def hash_texts(texts):

    for text in texts:

        print("\nText: " + text)

        try:

            md5 = hash_md5(text)
            sha1 = hash_sha1(text)
            sha224 = hash_sha224(text)
            sha256 = hash_sha256(text)

            print("MD5: " + md5)
            print("SHA-1: " + sha1)
            print("SHA-224: " + sha224)
            print("SHA-256: " + sha256)

        except:
            print("Error")

