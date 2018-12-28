#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    upper_indicator=1;
    lower_indicator=1;
    digit=1;
    special_character=1;
    for i in password:
        if i.islower():
            lower_indicator=0;
        elif i.isupper():
            upper_indicator=0;
        elif i.isdigit():
            digit=0;
        else:
            special_character=0;
    
    if (lower_indicator+upper_indicator+digit+special_character+len(password)<6):
        return (lower_indicator+upper_indicator+digit+special_character) + (6-(lower_indicator+upper_indicator+digit+special_character+len(password)));
    else:
        return (lower_indicator+upper_indicator+digit+special_character);

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
