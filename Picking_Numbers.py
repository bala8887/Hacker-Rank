#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
# Write your code here
    lst=[];
    tmp_lst=[];
    a.sort();
    for x in range(len(a)):
        #print (x);
        i=a[x];
        #print (i);
        if len(tmp_lst)==0:
            min_element=i;
        else:
            min_element=min(tmp_lst);
        if i-min_element>=2:
            lst.append(tmp_lst);
            tmp_lst=[];
            tmp_lst.append(i);
        else:
            tmp_lst.append(i);

    max1=0;
    for i in lst:
        if(len(i)>max1):
            max1=len(i);
    if max1==0:
        return len(a);
    else:
        return max1;

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()


