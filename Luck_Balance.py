#!/bin/python3

import math
import os
import random
import re
import sys

from operator import itemgetter

# Complete the luckBalance function below.
def luckBalance(k, contests):
    contests.sort(key=itemgetter(0));
    contests.reverse();
    total=0;
    for i in contests:
        if i[1]==0:
            total+=i[0];
        else:
            if k>0:
                total+=i[0];
            else:
                total-=i[0];
            k=k-1;
        
    return total;

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
