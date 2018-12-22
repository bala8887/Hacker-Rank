#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cavityMap function below.
def cavityMap(grid):
    result=[];
    for i in range(len(grid)):
        result.append(list(grid[i]));
    
    for i in range(len(result)):
        for j in range(len(result[i])):
            if (j!=0) and (j!=len(result[i])-1) and (i!=0) and (i!=len(result)-1):
                #result[i]=result[i][0]+result[i][1:len(grid[i])-1].replace('9','X')+result[i][len(grid[i])-1];
                if result[i][j+1]<result[i][j] and result[i][j-1]<result[i][j] and result[i+1][j]<result[i][j] and result[i-1][j]<result[i][j]:
                    result[i][j]='X';
    
    result1=[];
    for i in range(len(result)):
        result1.append("".join(result[i]));
    return result1;

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

