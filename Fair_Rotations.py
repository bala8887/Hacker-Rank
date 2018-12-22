#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the fairRations function below.
def fairRations(B):
    total=0;
    if sum(B)%2==0:
        if sum([1 for x in B if x%2!=0])>0:
            for i in range(len(B)):
                if B[i]%2==1:
                    B[i]+=1;
                    B[i+1]+=1;
                    total+=2;
            return total;
        else:
            return 0;
    else:
        return "NO";

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(str(result) + '\n')

    fptr.close()

