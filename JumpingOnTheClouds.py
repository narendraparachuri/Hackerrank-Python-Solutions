#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps=0
    curpos=0
    endpos=len(c)-1
    while curpos < endpos:
        if ((curpos+2) <= endpos) and (c[curpos+2]==0):
            curpos+=2
            jumps+=1
        elif (c[curpos+1] == 0):
            curpos+=1
            jumps+=1
    return jumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
