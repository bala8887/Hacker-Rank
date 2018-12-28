#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the decentNumber function below.
def decentNumber(n):
    three=0
    five=0
    #if n%3==0:
    #    five=n//3;
    #    print ('5'*five);
    #elif n%5==0:
    #    three=n//5;
    #    print ('3'*three);
    #else:
    #indicator=0;
    #while indicator==0 and n>0:
        #print (n);
        #n=n-5;
        #three+=5;
    #    if n%3==0:
    #        #print ("if");
    #       five=n;
    #        indicator=1;
    #        print (('5'*five)+('3'*three));
    #        break;
    #    elif n%5==0:
    #        three=n;
    #        indicator=1;
    #        print (('5'*five)+('3'*three));
    #        break;
    #    else:
    #        n=n-5;
    #        three=three+5;
    #        if n%3==0:
    #            five=n;
    #            indicator=1;
    #            print (('5'*five)+('3'*three));
    #if indicator==0:
    #   print (-1);
        
    tmp_n=n;
    while (n>0 and n%3!=0):
        n=n-5;
    if n<0:
        print (-1);
    else:
        print (('5'*n)+('3'*(tmp_n-n)));

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        decentNumber(n)
