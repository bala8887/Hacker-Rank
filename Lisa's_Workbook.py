#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the workbook function below.
def workbook(n, k, arr):
    lst=[]; page=1; total=0;
    for i in arr:
        pblm=0;
        while pblm!=i:
            if (pblm+k)<i:
                lst.append(list(range(pblm,pblm+k)));
                print (lst);
                pblm+=k;
            else:
                lst.append(list(range(pblm,i)));
                print (lst);
                pblm+=(i-pblm);

    for j in range(len(lst)):
        if j in lst[j]:
            total+=1;
    return total;
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

