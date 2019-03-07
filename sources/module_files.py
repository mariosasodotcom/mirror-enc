#!/usr/bin/env python


import os
import aes_encryption
import hash_algorithms
import encoding_func


def menu():

    menu = """
    [1.] AES Encryption   [ AES-128, AES-192, AES-256 ]
    [2.] HASH Algorithms  [ MD5, SHA-1, SHA-224, SHA-256 ]
    [3.] BASE64 Encoding  [ FILE(S) <=> STRING(S) ]
    [CTRL + C] EXIT mirror-enc  
    """

    print(menu)

    x = '0'

    while x not in ['1', '2', '3']:
        x = str(raw_input("mirror-enc > "))

    return x



def files_or_folders(argv_list):

    files = []
    folders = []

    for element in argv_list:

        if element != argv_list[0]:

            if os.path.isfile(element) == True:
                files.append(element)

            elif os.path.isdir(element) == True:
                folders.append(element)

    return files, folders



def search_file(folder):

    file_paths = []

    for root, directories, files in os.walk(folder):

        for filename in files:

            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

    return file_paths



def main(argv_list):

    files, folders = files_or_folders(argv_list)
    choose = menu()

    if choose == '1':        # AES Encryption

        key = aes_encryption.choose_key()
        alg = aes_encryption.enc_dec(key)

        if alg == "enc":

            aes_encryption.encrypt_list(files, key)

            for folder in folders:

                files = search_file(folder)

                aes_encryption.encrypt_list(files, key)

        elif alg == "dec":

            aes_encryption.decrypt_list(files, key)

            for folder in folders:

                files = search_file(folder)

                aes_encryption.decrypt_list(files, key)

    elif choose == '2':        # HASH Algorithms

        hash_algorithms.hash_list(files)

        for folder in folders:

            files = search_file(folder)

            hash_algorithms.hash_list(files)

    elif choose == '3':        # Encoding Function

        alg = encoding_func.enc_dec()

        if alg == "enc":

            encoding_func.enc_files(files)

            for folder in folders:

                files = search_file(folder)

                encoding_func.enc_files(files)

        elif alg == "dec":

            encoding_func.dec_files(files)

            for folder in folders:

                files = search_file(folder)

                encoding_func.dec_files(files)









