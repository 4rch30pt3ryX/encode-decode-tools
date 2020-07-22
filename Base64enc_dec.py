#!usr/bin/env python
"""
                        *******************************
                        *   Created by 4rch30pt3ryX   *
                        *******************************

Base64 converter for injection, or other things I suppose.
"""
import base64
import os
from colorama import init, Fore, Back, Style
from termcolor import colored

# ex: inj = '1 OR 1 = 1
def encode():
    text = colored("\n   string to be encoded: ", "green")
    texts = raw_input(text)
    bsixfour = base64.b64encode(texts)
    print((colored('   base64 encoded string: ', 'green')) + bsixfour)
    exit()

def decode():
    base = colored("\n   base64 to be decoded: ", "green")
    bases = raw_input(base)
    decoded = base64.b64decode(bases)
    print((colored('   base64 decoded string: ', 'green')) + decoded)
    exit()

def startpage():
    import conRepo_v_1_3.py

def signage():
    init()
    print('\n\n')
    print(colored('   *************************************', 'magenta'))
    print(colored('   *    - Created By 4rch30pt3ryX -    *', 'magenta'))
    print(colored('   *************************************', 'magenta'))
    print('\n')

def intent():
    signage()
    introen = colored("encode", "green") + colored(", ", "cyan")
    introde = colored("decode", "green") + colored(", ", "cyan")
    intrmain = colored("main", "magenta") + colored(", or ", "cyan")
    introquit = colored("quit", "red") + colored(".\n", "cyan")
    intro1 = colored("   Welcome to the base64 encoder and decoder.\n", "cyan")
    intro2 = colored("   Would you like to encode a string to Base64 or\n",
                     "cyan")
    intro3 = colored("   decode from Base64 to a string?\n", "cyan")
    intro4 = colored("   Type ", "cyan") + introen + introde + intrmain + introquit
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
            elif str(user) =='main':
                startpage()
            elif str(user) != 'encode' or 'decode' or 'quit':
                usr = colored(str(user, "red"))
                apo = colored(" Apologies, but ", "green")
                novalid = colored(" is not a valid command. \n Try again or maybe you should quit",
                                  "green")
                print(apo + usr + novalid)
        except Exception:
            usr = colored(user, "red")
            apo = colored(" Apologies, but ", "green")
            novalid = colored(" is not a valid command. \n Try again or maybe you should quit","green")
            print(apo + usr + novalid) 
intent()
