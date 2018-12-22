#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    lst=[];
    min_element=0;
    
    while True:
        lst.append(len(arr));
        min_element=min(arr);
        arr=[x for x in arr if x!=min_element];
        arr=[x-min_element for x in arr];
        if arr.count(min_element)==len(arr):
            if len(arr)>0:
                lst.append(len(arr));
            break;
    

    #lst.append()
    return lst;

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

