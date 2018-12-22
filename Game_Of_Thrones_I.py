#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gameOfThrones function below.
def gameOfThrones(s):
    odd_indicator=len(s)%2;
    ind=0;
    first_ind=0;
    for i in set(s):
        if (s.count(i))%2==1:
            if odd_indicator==1 and first_ind==0:
                first_ind=1;
            else:
                ind=1;
                break;
    if ind==0:
        return 'YES';
    else:
        return 'NO';

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()

