#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pairs=0
    loop=0
    ar.sort()
    ar.append('*')
    while (loop<n):
        if ar[loop]==ar[loop+1]:
            pairs+=1
            loop+=2
        else:
            loop+=1
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
