#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#
def insertionSort1(start, arr):
    f = arr[start]
    
    for x in range(start-1, -1, -1):
        if arr[x] > f:
            arr[x+1] = arr[x]
        else:
            arr[x+1] = f
            break
    if arr[0] > f:
        arr[0] = f

def insertionSort2(n, arr):
    # Write your code here
    for y in range(1, len(arr)):
        insertionSort1(y, arr)
        print(" ".join(map(str, arr)))
        
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
