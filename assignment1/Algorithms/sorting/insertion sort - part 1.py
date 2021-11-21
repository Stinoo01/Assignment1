#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    f = arr[-1]
    
    for x in range(len(arr)-2, -1, -1):
        if arr[x] > f:
            arr[x+1] = arr[x]
            print(" ".join(map(str, arr)))
        else:
            arr[x+1] = f
            print(" ".join(map(str, arr)))
            break
    if arr[0] > f:
        arr[0] = f
        print(" ".join(map(str, arr)))
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)