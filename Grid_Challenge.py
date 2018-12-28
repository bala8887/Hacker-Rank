#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gridChallenge function below.
def gridChallenge(grid):
    for i in grid:
        i.sort();
    for i in range(len(grid[0])):
        tmp_grid=[x[i] for x in grid]
        sort_grid=tmp_grid.copy();
        sort_grid.sort();
        if sort_grid!=tmp_grid:
            return "NO";
    return "YES";

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(list(grid_item))

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
