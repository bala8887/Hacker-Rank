#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    indicator=0;
    lst=list(s);
    while indicator==0:
        indicator=1;
        for i in range(len(lst)-1):
            if lst[i]==lst[i+1]:
                indicator=0;
                lst.pop(i);
                lst.pop(i);
                break;
            #if indicator==1:
            #    indicator=0;
            #else:
            #    indicator=1;
    if len(lst)==0:
        return "Empty String";
    else:
        return ''.join(lst);

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
