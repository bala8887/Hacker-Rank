#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    result_string="hackerrank";
    j=0;
    for i in s:
        if j<len(result_string) and result_string[j]==i:
            j+=1;
    if j==len(result_string):
        return "YES";
    else:
        return "NO";

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
