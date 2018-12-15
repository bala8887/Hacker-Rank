#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    diag_sum_1,diag_sum_2=0,0;
    size=len(arr);
    for i in range(size):
        diag_sum_1=diag_sum_1+arr[i][i];
        diag_sum_2=diag_sum_2+arr[i][size-i-1];
    return abs(diag_sum_1-diag_sum_2);

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

