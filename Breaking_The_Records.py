#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    min_score,max_score,min_record,max_record=0,0,0,0;
    min_score=scores[0];
    max_score=scores[0];
    for i in range(len(scores)):
        if i>0:
            if scores[i]>max_score:
                max_score=scores[i];
                max_record+=1;
            if scores[i]<min_score:
                min_score=scores[i];
                min_record+=1;
    return ([max_record,min_record]);   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

