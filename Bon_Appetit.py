#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
    #annaBill = sum(ar[i] for i in range(n) if i != k)//2
    #return 'Bon Appetit' if annaBill == b else str(b-annaBill)
def bonAppetit(bill, k, b):
    original_bill=sum(bill[i] for i in range(len(bill)) if i != k)//2
    #sum[bill[x] for x in range(len(bill)) if x!=k]//2;

    if b==original_bill:
        print('Bon Appetit');
    else:
        print(int(b-original_bill));
    
if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
    
 
