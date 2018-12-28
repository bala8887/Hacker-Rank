#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    #return len(s)-(s.count('S')+s.count('O'));
    count=0;
    for i in range(0,len(s),3):
        tmp_string=s[i:i+3];
        if tmp_string[0]!='S':
            count+=1;
        if tmp_string[1]!='O':
            count+=1;
        if tmp_string[2]!='S':
            count+=1;
    return count;


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
