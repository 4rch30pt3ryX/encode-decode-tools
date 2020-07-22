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

def signage():
    import signage2

#----------------------Main Page------------------------#

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
    
    intrbase = colored("base64", "green") + colored(", ", "cyan")
    intrhex = colored("hex", "green") + colored(", ", "cyan")
    intrrot = colored("rot13", "green") + colored(", or ", "cyan")
    intrbin = colored("\n   binary", "green")
    intrquit = colored("quit", "red") + colored(".", "cyan")
    intro1 = colored("\n   Welcome to a collection of decoders", "cyan")
    intro2 = colored("\n   & encoders. Type ", "cyan")
    intro3 = intrbase + intrhex + intrrot
    intro4 = intrbin + colored("   to decode or encode with it.", "cyan")
    intro5 = colored("\n   Alternatively, you can type ", "cyan") + intrquit
    print(intro1 + intro2 + intro3 + intro4 + intro5)
    usrin = "\n   [-->: "
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
