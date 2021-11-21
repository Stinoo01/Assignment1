#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    count = [0] * (max(arr) + 1)
    output = [0] * (len(arr))
    total = 0
    for x in arr:
        count[x] += 1
    for ind in range(len(count)):
        old = count[ind]
        count[ind] = total
        total += old
    for y in arr:
        output[count[y]] = y
        count[y] += 1
        
    return output
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
