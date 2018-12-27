#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort2 function below.
def insertionSort2(n, arr):
    for i in range(len(arr)-1):
        for j in range(i+1,0,-1):
            if arr[j]<arr[j-1]:
                tmp=arr[j-1];
                arr[j-1]=arr[j];
                arr[j]=tmp;
        print (' '.join(str(x) for x in arr));

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
