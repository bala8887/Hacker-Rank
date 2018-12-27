#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    #arr=[2,4,6,8,3];
    n=arr[len(arr)-1];
    if arr[len(arr)-2]<=arr[len(arr)-1]:
        lst=[]
        for i in arr:
            lst.append(i);
            #lst.append(n);
            print (lst);
    else:
        #arr.append(arr[len(arr)-1]);
        indicator=0;
        arr[len(arr)-1]=arr[len(arr)-2];
        for i in range(len(arr)):
            lst=[]; k=len(arr)-i-1;
            #print (k);
            for j in range(len(arr)):
                if k==j:
                    #print (k);
                    if arr[k]>n and arr[k-1]>n and k>0: #arr[len(arr)-i-1]==arr[i]:
                        lst.append(arr[k-1]);
                    else:
                        lst.append(n);
                        indicator=1;
                else:
                    lst.append(arr[j]);
            print (' '.join(str(x) for x in lst));
            arr=lst;
            if indicator==1:
                break;

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
