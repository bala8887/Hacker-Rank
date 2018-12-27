#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the runningTime function below.
def runningTime(arr):
    tmp_arr=arr.copy();
    tmp_arr.sort();
    total=0;
    for i in range(1,len(arr)):
        for j in range(i,0,-1):
            print (j);
            if arr[j]<arr[j-1]:
                tmp=arr[j];
                arr[j]=arr[j-1];
                arr[j-1]=tmp;
                total+=1;
        if tmp_arr==arr:
            return total;
            break;


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
