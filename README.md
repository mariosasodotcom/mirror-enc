# mirror-enc
```
    
     ___________ @ @                                                     
    /   v1.0   @\   @                       _                            
    \___________/  _@              ___ __ _(_)__ _ __ _  ___ __ _        
              @  _/@ \_____       / _ ' _` | |__` |__` |/ _ \__` |       
               @/ \__/-=-=^`     | | | | | | |  | |  | | (_) | | |       
                \_ /             |_| |_| |_|_|  |_|  |_|\___/  |_|-enc   
                 <|                                                      
                 <|                    github.com/M4R1OS4S0              
                 <|                                                     

```

### Repo Overview
```

│   mirror-enc.py          start mirror-enc
│   sources                source code of the tool
│   README.md              project readme
│   LICENSE                license of the tool
│   .gitignore             gitignore for the python program   
└───
```

### Usage
```
python mirror-enc.py -f FILE or FOLDER (1), FILE or FOLDER (2), ... , FILE or FOLDER (n)    # FILES MODE

python mirror-enc.py -t TEXT (1), TEXT (2), ... , TEXT (n)                                  # TEXTS MODE   
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
This module uses MD5, SHA-1, SHA-224 and SHA-256 algorithms to generate hashes 
```

BASE64 Encoding:
```
This module uses Base64 to encode or decode (if text files) files
```

### Texts Mode

AES Encryption:
```
This module uses Advanced Encryption Standard (AES) to encrypt and decrypt texts.
Encrypted chipertext will be (or must be, if as input) encoded with Base64.
The key which is used to encrypt should be same as the key that will be used for decrypt. 
Change the AES key lenght either 16, 24 or 32 bytes to select AES-128, AES-192 or AES-256.
```

HASH Algorithm:
```
This module uses MD5, SHA-1, SHA-224 and SHA-256 algorithms to generate hashes 
```

BASE64 Encoding:
```
This module uses Base64 to encode or decode texts
```
