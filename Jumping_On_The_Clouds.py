#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    total=0;
    i=0;
    while i<len(c)-1:
        if (i+2 <= len(c)-1) and (c[i+2]!=1):
            i+=2;
        else:
            i+=1;
        total+=1;
    return total;
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()

