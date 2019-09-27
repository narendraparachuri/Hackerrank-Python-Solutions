#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    timepart=s.split(":")
    if s[-2:]=="PM":
        if timepart[0]!="12":
            timepart[0]=str(int(timepart[0])+12)
    else:
        if timepart[0]=="12":
            timepart[0]="00"
    militarytime=':'.join(timepart)
    return str(militarytime[:-2])

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
