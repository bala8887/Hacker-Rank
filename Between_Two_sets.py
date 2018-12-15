#!/bin/python3

import os
import sys

#
# Complete the getTotalX function below.
#
def getTotalX(a, b):
    #
    # Write your code here.
    #
    max_a=max(a);
    min_b=min(b);
    x,y=0,0;
    lst=[];

    for i in range(max_a,min_b+1):
        for j in a:
            if i%j!=0:
                x=1;
                break;
        if x==0:    
            #lst.append(i);
            for k in b:
                if (k%i)!=0:
                    y=1;
                    break;
            if (y==0):
                lst.append(i);
            y=0;
        x=0;    
    
    #for i in b:
    #    if ():
    return len(lst);
 

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()

