#!/bin/python3

import math
import os
import random
import re
import sys

def hourglassSum(arr):
       
    max_sum=-999999999
    for row in range(len(arr)):
        temp_sum=0
        for col in range(len(arr[row])):
            if col+2>=len(arr[row]) or row+2>=len(arr[col]):
                continue
            temp_sum=arr[row][col] + arr[row][col+1] + arr[row][col+2] + arr[row+1][col+1] + arr[row+2][col] + arr[row+2][col+1] + arr[row+2][col+2]
            if max_sum < temp_sum:
                max_sum=temp_sum
    return max_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
