#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    lst=[];
    for i in s:
        lst.append(ord(i));
    
    tmp_lst=[];
    for i in range(len(lst)-1):
        tmp_lst.append(abs(lst[i]-lst[i+1]));

    indicator=0;
    for i in range(len(tmp_lst)//2):
        if tmp_lst[i]!=tmp_lst[len(tmp_lst)-i-1]:
            indicator=1;
            break;
    
    if indicator==0:
        return 'Funny';
    else:
        return 'Not Funny';


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
