#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    if len(set(arr))==len(arr):
        return len(arr)-1;
    else:
        max=0;
        for i in set(arr):
            max = arr.count(i) if max<arr.count(i) else max;
        return len(arr)-max;

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

