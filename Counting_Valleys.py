#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    level=0;
    indicator=0;
    times=0;
    for i in s:
        if i=='D':
            level-=1;
            if level<0:
                indicator=1;
        else:
            level+=1;
            if (level==0) and (indicator==1):
                times+=1;
                indicator=0;
    return times;
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

