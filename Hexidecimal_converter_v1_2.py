#!user/bin/env python

# -*- coding: utf-8 -*-
"""

                        *******************************
                        *   Created by 4rch30pt3ryX   *
                        *******************************

Simple hexidecimal encoder/decoder
"""
import sys
from colorama import init, Fore, Back, Style
from termcolor import colored

keyList = []
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
            endisp = colored("   integer to be converted: ", "green")
            usrin = raw_input(endisp)
            usrtext = int(usrin)
            hexed = hex(usrtext)
            conv = (colored("\n   number to be converted: ", "magenta"))
            print(conv + (colored(usrtext, 'blue') + '\n'))
            hexer = (colored("   hexidecimal encoding: ", "magenta"))
            print(hexer + (colored(hexed, 'green')))                    
            sys.exit()
        except Exception:
            print(colored("\n   that is not an integer...\n", "red"))
            intent()

def decode():
    #TODO: try statement to handle bad user input (not hex for decode)
    dedisp = colored("\n   hexidecimal code to be converted: ", "green")
    usrsin = raw_input(dedisp)
    dectext = int(usrsin, 0)
    deconv = (colored("\n   hex to be converted: ", "magenta"))
    print(deconv + (colored(usrsin, 'blue') + '\n'))
    dehexer = (colored("   Integer Form: ", "magenta"))
    print(dehexer + (colored(dectext, 'green')))                    
    sys.exit()

def starter():
    import conRepo_v_1_3.py

def intent():        
    introen = colored("encode", "green") + colored(", ", "cyan")
    introde = colored("decode", "green") + colored(", ", "cyan")
    intromain = colored("main", "magenta") + colored(", or ", "cyan")
    introquit = colored("quit", "red") + colored(".\n", "cyan")
    intro1 = colored("   Welcome to the Hexidecimal encoder and decoder.\n",
                     "cyan")
    intro2 = colored("   Would you like to encode an integer to hexidecimal or\n",
                     "cyan")
    intro3 = colored("   decode from hexidecimal to an integer?\n", "cyan")
    intro4 = colored("   Type ", "cyan") + introen + introde + intromain + introquit 
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
                starter()
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
    
def assign(self):
    keylist = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
               'n','o','p','q','r','s','t','u','v','w','x','y','z',
               'A','B','C','D','E','F','G','H','I','J','K','L','M',
               'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
               '0','1','2','3','4','5','6','7','8','9','!','@','#',
               '$','%','^','&','*','(',')','_','+','-','=','{','}',
               '[',']','\\','|',';',':','\'','"','/','?','.','>','<',
               ',','~','`']                     
intent()
