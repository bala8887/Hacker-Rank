#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    total=0;
    for x in range(i,j+1):
        y=list(str(x));
        y.reverse();
        z=int(''.join(str(a) for a in y));
        #return z;

        if abs(z-x)%k==0:
            total+=1;
    return total;


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()

