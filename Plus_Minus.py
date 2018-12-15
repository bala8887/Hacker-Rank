#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    arr.sort();
    pos=len(arr);
    for i in range(len(arr)):
        if arr[i]>0:
            pos=i;
            break;
        
    
    #pos=arr.index(0);
    print ('%.6f' % ((len(arr)-pos)/len(arr)));
    print ('%.6f' % ((pos-arr.count(0))/len(arr)));
    print ('%.6f' % (arr.count(0)/len(arr)));
    

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

