#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'runningTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def insertionSort1(start, first):
    probe = first[start]
    output = 0
    
    for x in range(start-1, -1, -1):
        if first[x] > probe:
            output += 1
            first[x+1] = first[x]
        else:
            first[x+1] = probe
            break
    if first[0] > probe:
        first[0] = probe
        
    return output

def insertionSort2(n, second):
    result = 0
    for y in range(1, len(second)):
        result += insertionSort1(y, second)
    return result

def runningTime(arr):
    # Write your code here
    return insertionSort2(len(arr), arr)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
