#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulTriplets function below.
def beautifulTriplets(d, arr):
#    lst=[]; total=0;
#    for i in arr:
#        for j in arr:
#            if j-i==d:
#                lst.append([i,j]);
#               print (i,j);
#    for i in range(len(lst)):
#        for j in range(1,len(lst)):
#            if lst[i][1]==lst[j][0]:
#                total+=1;
#    return total;

#Good Solution to note it down
    gc=0;
    for i in range(n):
        if arr[i]+d in arr and arr[i]+2*d in arr:
            gc+=1;
    return gc;

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

