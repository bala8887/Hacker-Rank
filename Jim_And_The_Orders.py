#!/bin/python3

import math
import os
import random
import re
import sys
from operator import itemgetter

# Complete the jimOrders function below.
def jimOrders(orders):
    lst=[];
    tmp_lst=[];
    j=1;
    for i in orders:
        lst.append([j,i[0]+i[1]]);
        j+=1;
    lst.sort(key=itemgetter(1));
    
    for j in lst:
        tmp_lst.append(j[0]);
    return tmp_lst;

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
