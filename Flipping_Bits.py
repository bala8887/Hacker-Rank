#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flippingBits function below.
def flippingBits(n):
    binary='{0:b}'.format(n);
    binary_32='0'*(32-len(binary))+binary;
    tmp1=binary_32.replace('0','2');
    tmp2=tmp1.replace('1','0');
    tmp3=tmp2.replace('2','1');
    return int(tmp3,2);

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
