#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k, n):
    moves=math.ceil(n/k);
    i=0;
    thunder=0;
    while i<n:
        if c[i]==1:
            thunder+=1;
        i=i+k;
    return 100-(thunder*2)-(moves);

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k,n)

    fptr.write(str(result) + '\n')

    fptr.close()

