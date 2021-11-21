#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
'''
in Hackerrank s.split() and s.replace() work, but when I run it in my Python it does not recognize them 
'''
def solve(s):
    for x in s.split():
        s = s.replace(x,x.capitalize())
    return s
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
