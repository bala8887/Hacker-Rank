#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
def caesarCipher(s, k):
    lst=[];
    k=k%26;
    for i in s:
        if i.islower():
            if ord(i)+k <= ord('z'):
                lst.append(chr(ord(i)+k));
            else:
                lst.append(chr(ord(i)+k-26));
        elif i.isupper():
            if ord(i)+k <= ord('Z'):
                lst.append(chr(ord(i)+k));
            else:
                lst.append(chr(ord(i)+k-26));
        else:
            lst.append(i);
    return ''.join(lst);

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
