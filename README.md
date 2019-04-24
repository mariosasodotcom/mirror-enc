# mirror-enc
```   
     ___________ @ @                                                     
    /          @\   @                       _                            
    \___________/  _@              ___ __ _(_)__ _ __ _  ___ __ _        
              @  _/@ \_____       / _ ' _` | |__` |__` |/ _ \__` |       
               @/ \__/-=-=^`     | | | | | | |  | |  | | (_) | | |       
                \_ /             |_| |_| |_|_|  |_|  |_|\___/  |_|-enc   
                 <|                                                      
                 <|                    github.com/M4R1OS4S0              
                 <|                                                     
```

### License
```
MIRROR-ENC IS LICENSED UNDER THE GNU GENERAL PUBLIC LICENSE v3.
```

### Requirements
```
Python 2 and Pycrypto must be installed on your computer.
```

### Repo Overview
```
│   mirror-enc.py          start mirror-enc
│   modules                source code of the tool
│   README.md              project readme
│   LICENSE                license of the tool
│   .gitignore             gitignore for the python program   
└───
```

### Usage
```
$ python mirror-enc.py    
```

### Chat Mode
```
This module performs a simple encrypted chat on LAN that combines RSA and AES algorithms.  
```


### Texts Mode

RSA Encryption:
```
This module uses Rivest–Shamir–Adleman (RSA) to encrypt and decrypt texts.
A Public Key is used to encrypt texts and a Private Key is used to decrypt texts.
```

AES Encryption:
```
This module uses Advanced Encryption Standard (AES) to encrypt and decrypt texts.
Encrypted chipertext will be (or must be, if as input) encoded with Base64.
The key which is used to encrypt should be same as the key that will be used for decrypt. 
Change the AES key lenght either 16, 24 or 32 bytes to select AES-128, AES-192 or AES-256.
```

HASH Algorithm:
```
This module uses MD5, SHA-1, SHA-224 and SHA-256 algorithms to generate hashes.
```

BASE64 Encoding:
```
This module uses Base64 to encode or decode texts.
```

### Files Mode

AES Encryption:
```
This module uses Advanced Encryption Standard (AES) to encrypt and decrypt files. 
The key which is used to encrypt should be same as the key that will be used for decrypt. 
Change the AES key lenght either 16, 24 or 32 bytes to select AES-128, AES-192 or AES-256.
```

HASH Algorithm:
```
This module uses MD5, SHA-1, SHA-224 and SHA-256 algorithms to generate hashes.
```

BASE64 Encoding:
```
This module uses Base64 to encode or decode files (if text files).
```

### Gen Mode
```
This module generates random AES keys and RSA keypairs.
```
