#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    x=0;
    length=min(len(s),len(t));
    for i in range(length):
        if s[0:i+1]!=t[0:i+1]:
            x=i;
            break;
        if i==length-1:
            x=i+1;

    if (len(s)-x)+(len(t)-x)<=k:
        if (len(s)<len(t)) and (x+len(t)>k) and ((len(t)-x)%2!=k%2):
            return "No";
        else:
            return "Yes";
    else:
        return "No";

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()

