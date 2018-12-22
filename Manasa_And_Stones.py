#!/bin/python3

import math
import os
import random
import re
import sys
#Good program to think about the logic
#For example, if there are 8 different paths then 
# Complete the stones function below.
def stones(n, a, b): #0 1 2
    lst=[];
    for i in range(n-1):
        lst.append(a);
    if a!=b:
        final_lst=[];
        for i in range(n-1):
            final_lst.append(sum(lst));
            lst[i]=b;
        final_lst.append(sum(lst));
        final_lst.sort()
        return final_lst;
    else:
        final_lst=[];
        final_lst.append(sum(lst));
        return final_lst;

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        n = int(input())

        a = int(input())

        b = int(input())

        result = stones(n, a, b)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

