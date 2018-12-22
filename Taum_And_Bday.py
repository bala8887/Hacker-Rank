#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the taumBday function below.
def taumBday(b, w, bc, wc, z):
    min_value=0;
    if bc==wc:
        return (b+w)*bc;
    elif (min(bc,wc) + z) > max(bc,wc):
        return (bc*b)+(wc*w);
    else:
        min_value=min(bc,wc);
        max_product=w if min_value==bc else b;
        return ((b+w)*min_value)+(z*max_product);

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        bw = input().split()

        b = int(bw[0])

        w = int(bw[1])

        bcWcz = input().split()

        bc = int(bcWcz[0])

        wc = int(bcWcz[1])

        z = int(bcWcz[2])

        result = taumBday(b, w, bc, wc, z)

        fptr.write(str(result) + '\n')

    fptr.close()

