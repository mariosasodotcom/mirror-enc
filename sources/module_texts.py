#!/usr/bin/env python


import aes_encryption
import hash_algorithms
import encoding_func


def menu():

    menu = """
    [1.] AES Encryption   [ AES-128, AES-192, AES-256 ]
    [2.] HASH Algorithms  [ MD5, SHA-1, SHA-224, SHA-256 ]
    [3.] BASE64 Encoding  [ TEXT(S) <=> STRING(S) ]
    [CTRL + C] EXIT mirror-enc  
    """

    print(menu)

    x = '0'

    while x not in ['1', '2', '3']:
        x = str(raw_input("mirror-enc > "))

    return x



def texts_list(argv_list):

    texts = []

    for element in argv_list:

        if element != argv_list[0] and element != argv_list[1]:

            texts.append(element)

    return texts



def main(argv_list):

    texts = texts_list(argv_list)
    choose = menu()

    if choose == '1':        # AES Encryption

        key = aes_encryption.choose_key()
        alg = aes_encryption.enc_dec(key)

        if alg == "enc":

            aes_encryption.encrypt_texts(texts, key)

        elif alg == "dec":

            aes_encryption.decrypt_texts(texts, key)

    elif choose == '2':        # HASH Algorithms

        hash_algorithms.hash_texts(texts)

    elif choose == '3':        # Encoding Function

        alg = encoding_func.enc_dec()

        if alg == "enc":

            encoding_func.enc_texts(texts)

        elif alg == "dec":

            encoding_func.dec_texts(texts)








