##!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    #creating the variable which will contain our message
    ciphered_message = ""

    #loop that shift the letters:
    #for each letter:
    for folklore in s:
        #since the input will only have lower characters
        #letters are in lowercase
        if folklore.islower():
            #shifting:
            #keeping in mind that we are using the english alphabet (26 letters)
            #creating the current index
            evermore_index = ord(folklore) - ord('a')
            #creating the new index with the shifting
            new_index = (evermore_index + k) % 26
            new_shift = new_index + ord('a')
            new_character = chr(new_shift)
            ciphered_message = ciphered_message + new_character
        elif folklore.isupper():
            evermore_index = ord(folklore) - ord('A')
            #creating the new index with the shifting
            new_index = (evermore_index + k) % 26
            new_shift = new_index + ord('A')
            new_character = chr(new_shift)
            ciphered_message = ciphered_message + new_character
        else:
            ciphered_message += folklore
    
    #printing result
    return ciphered_message

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
