#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    initial_string='';
    ind=0;
    total=0;

    if len(s)==s.count('A') or len(s)==s.count('B'):
        return len(s)-1;
    
    for i in s:
        if ind==0:
            ind=1;
            initial_string=i;
        else:
            if initial_string==i:
                total+=1;
            else:
                initial_string=i;
    return total;
         

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
