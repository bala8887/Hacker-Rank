#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the anagram function below.
def anagram(s):
    odd_indicator=len(s)%2;
    total=0;
    if odd_indicator==1:
        return -1;
    else:
        middle=len(s)//2;
        first=s[0:middle];
        second=s[middle:len(s)];
        for i in set(first):
            if first.count(i)-second.count(i)>0:
                total+=first.count(i)-second.count(i);
        return total;

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()

