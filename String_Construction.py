#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stringConstruction function below.
def stringConstruction(s):
    copy=[]; indicator=0; total=0;
    if len(set(s))==1:
        return 1;
    else:
        for i in range(len(s)):
            if indicator==0:
                copy.append(s[i]);
                indicator=1;
                total+=1;
            else:
                if s[i] in copy:
                    copy.append(s[i]);
                else:
                    copy.append(s[i]);
                    total+=1;
    return total;

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = stringConstruction(s)

        fptr.write(str(result) + '\n')

    fptr.close()
