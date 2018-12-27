#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
    max=0;
    indicator=0;
    for i in range(len(w)-1):
        if ord(w[i])<ord(w[i+1]):
            indicator=1;
    if indicator==0:
        return "no answer";
    lst=list(w);
    tmp_lst=[];
    final_lst=[];
    #element='';
    for i in range(len(lst)-1,0,-1):
        if lst[i]>lst[i-1]:
            print (lst[i]);
            print (lst[i-1]);
            tmp_lst=lst[i-1:];
            print (tmp_lst);
            tmp_lst.sort();
            for x in tmp_lst:
                if ord(x)>ord(lst[i-1]):
                    tmp_lst.remove(x);
                    break;
            print (tmp_lst);
            #tmp_lst.remove(element);
            final_lst=lst[0:i-1];
            print (final_lst);
            final_lst.append(x);
            print (final_lst);
            final_lst.extend(tmp_lst);
            #tmp=lst[i];
            #lst[i]=lst[i-1];
            #lst[i-1]=tmp;
            break;
    if len(lst)==2:
        return ''.join(lst[::-1]);
    else:
        return ''.join(final_lst);

        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
