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

#-----------------SIGNAGE-----------------#
ASCII_CHARS = [ '#', '?', '%', '.', 'S', '+', '.', '*', ':', ',', '@']

def scale_image(image, new_width=100):
    """Resizes an image preserving the aspect ratio.
    """
    (original_width, original_height) = image.size
    aspect_ratio = original_height/float(original_width)
    new_height = int(aspect_ratio * new_width)

    new_image = image.resize((new_width, new_height))
    return new_image

def convert_to_grayscale(image):
    return image.convert('L')

def map_pixels_to_ascii_chars(image, range_width=25):
    """Maps each pixel to an ascii char based on the range
    in which it lies on the grayscale.

    0-255 is divided into 11 ranges of 25 pixels each.
    """

    pixels_in_image = list(image.getdata())
    pixels_to_chars = [ASCII_CHARS[pixel_value/range_width] for pixel_value in
            pixels_in_image]

    return "".join(pixels_to_chars)

def convert_image_to_ascii(image, new_width=100):
    image = scale_image(image)
    image = convert_to_grayscale(image)

    pixels_to_chars = map_pixels_to_ascii_chars(image)
    len_pixels_to_chars = len(pixels_to_chars)

    image_ascii = [pixels_to_chars[index: index + new_width] for index in
            xrange(0, len_pixels_to_chars, new_width)]

    return "\n".join(image_ascii)

def handle_image_conversion(image_filepath):
    image = None
    try:
        image = Image.open(image_filepath)
    except Exception, e:
        print "Unable to open image file {image_filepath}.".format(image_filepath=image_filepath)
        print e
        return

    image_ascii = convert_image_to_ascii(image)
    print('\n\n')
    strimg =  str(image_ascii)
    print (colored(strimg, "magenta"))
    
def handler():
    image_file_path = 'Archie2.jpg'
    handle_image_conversion(image_file_path)

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
    handler()
    
    intrbase = colored("base64", "green") + colored(", ", "blue")
    intrhex = colored("hex", "green") + colored(", ", "blue")
    intrrot = colored("rot13", "green") + colored(", or ", "blue")
    intrbin = colored("\n binary", "green")
    intrquit = colored("quit", "red") + colored(".", "blue")
    intro1 = colored("\n Welcome to a collection of decoders", "blue")
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
