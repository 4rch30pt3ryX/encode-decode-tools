#!usr/bin/env python
"""
                        *******************************
                        *   Created by 4rch30pt3ryX   *
                        *******************************

Main UI for various simple encoders/decoders
"""
import os
from colorama import init, Fore, Back, Style
from termcolor import colored
from PIL import Image

def signage():
    """init()
    print('\n\n')
    print(colored('   *************************************', 'magenta'))
    print(colored('   *    - Created By 4rch30pt3ryX -    *', 'magenta'))
    print(colored('   *************************************', 'magenta'))
    print('\n')"""
    import img2ascii

def basesixfour():
    import Base64enc_dec.py

def hexed():
    import Hexidecimal_converter_v1_2.py
    
def rotthirteen():
    import rot13converter_v1_0.py

def binary():
    print("I am currently a placeholder for binary")

def startpage():
    signage()
    
    intrbase = colored("base64", "green") + colored(", ", "blue")
    intrhex = colored("hex", "green") + colored(", ", "blue")
    intrrot = colored("rot13", "green") + colored(", or ", "blue")
    intrbin = colored("\n binary", "green")
    intrquit = colored("quit", "red") + colored(".", "blue")
    intro1 = colored(" Welcome to a collection of decoders", "blue")
    intro2 = colored("\n & encoders. Type ", "blue")
    intro3 = intrbase + intrhex + intrrot
    intro4 = intrbin + colored(" to decode or encode with it.", "blue")
    intro5 = colored("\n Alternatively, you can type ", "blue") + intrquit
    print(intro1 + intro2 + intro3 + intro4 + intro5)
    usrin = "[-->: "
    while True:
        try:
            user = raw_input(usrin)
            if str(user) == 'base64':
                basesixfour()
            elif str(user) == 'hex':
                hexed()
            elif str(user) == 'rot13':
                rotthirteen()
            elif str(user) == 'binary':
                binary()
            elif str(user) == 'quit':
                exit()
        except Exception:
            print('whoops')
   
startpage()
