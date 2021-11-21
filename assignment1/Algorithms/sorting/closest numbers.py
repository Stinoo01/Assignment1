#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    # Write your code here
    output = []
    arr = sorted(arr)
    maxx = 10**7
    
    for x in range(1, len(arr)):
        diff = abs(arr[x-1] - arr[x])
        
        if diff < maxx:
            output = [(arr[x-1], arr[x])]
            maxx = diff
        elif diff == maxx:
            output.append((arr[x-1], arr[x]))
             
    result_ = [item for sublist in output for item in sublist]
       
    return result_

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
