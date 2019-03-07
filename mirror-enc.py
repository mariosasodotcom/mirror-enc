#!/usr/bin/env python


import sys
import sources.module_files as module_files
import sources.module_texts as module_texts


def banner():
    
    banner = """
    
     ___________ @ @                                                     
    /   v1.0   @\   @                       _                            
    \___________/  _@              ___ __ _(_)__ _ __ _  ___ __ _        
              @  _/@ \_____       / _ ' _` | |__` |__` |/ _ \__` |       
               @/ \__/-=-=^`     | | | | | | |  | |  | | (_) | | |       
                \_ /             |_| |_| |_|_|  |_|  |_|\___/  |_|-enc   
                 <|                                                      
                 <|                    github.com/M4R1OS4S0              
                 <|                                                     
    """

    print(banner)


def help():

    help = """
    Usage:

    python mirror-enc.py -f FILE or FOLDER (1), FILE or FOLDER (2), ... , FILE or FOLDER (n)    # FILES MODE

    python mirror-enc.py -t TEXT (1), TEXT (2), ... , TEXT (n)                                  # TEXTS MODE
    
    """

    modes = ['-f', '-t']

    if len(sys.argv) == 1 or sys.argv[1] not in modes:
        print(help)
        sys.exit()



def main():

    try:

        banner()
        help()

        if sys.argv[1] == '-f':
            module_files.main(sys.argv)

        elif sys.argv[1] == '-t':
            module_texts.main(sys.argv)

        print('')

    except KeyboardInterrupt:
        print('\n')
        sys.exit()



if __name__ == '__main__':
    main()




    



