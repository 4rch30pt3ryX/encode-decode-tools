#!user/bin/env python

# -*- coding: utf-8 -*-
"""

                        *******************************
                        *   Created by 4rch30pt3ryX   *
                        *******************************

Simple Rot13 Encoder/Decoder
"""
import sys
import random as rng
from colorama import init, Fore, Back, Style
from termcolor import colored

def signage():
    init()
    print('\n\n')
    print(colored('   *************************************', 'magenta'))
    print(colored('   *    - Created By 4rch30pt3ryX -    *', 'magenta'))
    print(colored('   *************************************', 'magenta'))
    print('\n')
signage()

def encode():
    while True:
        try:
            usrenc = colored("\n   string to be converted to rot13: ", "blue")
            inusr = raw_input(usrenc)
            enc = inusr.encode('rot13')
            result = colored("\n   rot13 encoded string: ", "magenta")
            print(result + enc)
            sys.exit()
        except Exception:
            print(colored("   ya done goofed boy,...", "red"))
            intent()
            
def decode():
    while True:
        try:
            usrdec = colored("\n   rot13 string to be decoded: ", "blue")
            outusr = raw_input(usrdec)
            dec = outusr.decode('rot13')
            reslt = colored("\n   rot13 decoded string: ", "magenta")
            print(reslt + dec)
            sys.exit()
        except Exception:
            print(colored("   ya done goofed boy,..", "red"))
            intent()

def start():
    import conRepo_v_1_3.py

def intent():
    introen = colored("encode", "green") + colored(", ", "cyan")
    introde = colored("decode", "green") + colored(", ", "cyan")
    introman = colored("main", "magenta") + colored(", or ", "cyan")
    introquit = colored("quit", "red") + colored(".\n", "cyan")
    intro1 = colored("\n   Welcome to the Rot13 encoder and decoder.\n",
                     "cyan")
    intro2 = colored("   Would you like to encode a string to rot13 or\n",
                     "cyan")
    intro3 = colored("   decode from rot13 to a string?\n", "cyan")
    intro4 = colored("   Type ", "cyan") + introen + introde + introman + introquit
    print(intro1 + intro2 + intro3 + intro4)
    userin = colored("   [-->: ", "white")
    while True:
        try:
            user = raw_input(userin)
            if str(user) == 'encode':
                encode()
            elif str(user) == 'decode':
                decode()
            elif str(user) == 'quit':
                exit()
            elif str(user) == 'main':
                start()
            elif str(user) != 'encode' or 'decode' or 'quit':
                usr = colored(str(user, "red"))
                apo = colored("   Apologies, but ", "green")
                novalid = colored("   is not a valid command. \n Try again or maybe you should quit",
                                  "green")
                print(apo + usr + novalid)
        except Exception:
            usr = colored(user, "red")
            apo = colored("   Apologies, but ", "green")
            novalid = colored("   is not a valid command. \n Try again or maybe you should quit","green")
            print(apo + usr + novalid)            
intent()
