### mirror-enc v1.0.0

<p align="center">
  <a href="https://github.com/M4R1OS4S0/mirror-enc">
    <img src="https://github.com/M4R1OS4S0/mirror-enc/blob/master/resources/logo.png" alt="Logo" width=787 height=254>
  </a>


  <p align="center">
    A cryptography toolkit that provide AES and RSA encryption algorithms
    <br>
    <a href="https://github.com/M4R1OS4S0/mirror-enc/issues/new?template=bug.md">Report bug</a>
    ·
    <a href="https://github.com/M4R1OS4S0/mirror-enc/issues/new?template=feature.md&labels=feature">Request feature</a>
  </p>
</p>


## Table of contents

- [What's included](#whats-included)
- [How it works](#how-it-works)
- [About me](#about-me)
- [Copyright and license](#copyright-and-license)

--------------------------------------------------------------------------------

## What's included

```
│   mirror-enc.py          start mirror-enc
│   resources              logo img
│   README.md              project readme
│   LICENSE                license of the tool
│   .gitignore             gitignore for the python program   
└───
```

--------------------------------------------------------------------------------

## How it works

```
Usage:    
    
    $ python mirror-enc.py --rsa-enc -k <pub_key_path> -s <plaintext_string>
    [RSA String Encryption]
    
    $ python mirror-enc.py --rsa-dec -k <prv_key_path> -s <ciphertext_string>
    [RSA String Decryption]
    
    $ python mirror-enc.py --rsa-gen -d <dir_path>
    [RSA Keypair Generator]
    
    $ python mirror-enc.py --aes-enc -k <key> -s <plaintext_string>
    [AES String Encryption]
    
    $ python mirror-enc.py --aes-dec -k <key> -s <ciphertext_string>
    [AES String Decryption]
    
    $ python mirror-enc.py --aes-enc -k <key> -f <plaintext_file_path>
    [AES File Encryption]
    
    $ python mirror-enc.py --aes-dec -k <key> -f <ciphertext_file_path>
    [AES File Decryption]
    
    $ python mirror-enc.py --get-hashes -s <string>
    [HASH String Calculator]
    
    $ python mirror-enc.py --get-hashes -f <file_path>
    [HASH File Calculator]
```

--------------------------------------------------------------------------------

## About me

**Bio**

My name is Mario and I'm 23 years old. I am a computer engineering student in Pisa and a music producer.

**Contact Me**

- Github: <https://github.com/M4R1OS4S0>
- E-mail: mariosaso@protonmail.com

--------------------------------------------------------------------------------

## Copyright and license

Copyright (C) 2019-2020 Mario Saso. Code released under the [GPLv3](https://github.com/M4R1OS4S0/mirror-enc/blob/master/LICENSE).
