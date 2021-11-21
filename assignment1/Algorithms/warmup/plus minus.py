#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    positive = 0
    negative = 0
    zero = 0

    for x in range (len(arr)):
        if arr[x] > 0:
            positive = positive + 1
        elif arr[x] < 0 :
            negative = negative + 1 
        else:
            zero = zero + 1

    print(float(positive / len(arr)))
    print(float(negative / len(arr)))
    print(float(zero / len(arr)))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
