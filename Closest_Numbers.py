#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
def closestNumbers(arr):
    arr.sort();
    lst=[];
    minimum=0;
    for i in range(1,len(arr)):
        if i==1:
            lst.append(arr[i-1]);
            lst.append(arr[i]);
            minimum=abs(arr[i]-arr[i-1]);
        else:
            if minimum > abs(arr[i]-arr[i-1]):
                minimum=abs(arr[i]-arr[i-1]);
                lst.clear();              
                lst.append(arr[i-1]);
                lst.append(arr[i]);
            elif minimum == abs(arr[i]-arr[i-1]):
                lst.append(arr[i-1]);
                lst.append(arr[i]);
            else:
                minimum=minimum;
    return lst;

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
