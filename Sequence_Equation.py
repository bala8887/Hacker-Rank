#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    lst=[];
    for i in range(len(p)):
        lst.append(0);
        p[i]=p[i]-1;
    #return p;

    for i in range(len(p)):
        lst[i]=p.index(p.index(i))+1;
    return lst;
    #return lst;


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

