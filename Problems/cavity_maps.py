#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cavityMap function below.
def cavityMap(grid):
    grid_copy = []
    grid_copy.extend(grid)
    for i in range( 1, len(grid) - 1 ):
        #print(grid[i])
        for j in range(1, len(grid) - 1 ):
            n           = int(grid[i][j])
            number_low  = int(grid[i-1][j])
            number_l    = int(grid[i][j-1])
            number_r    = int(grid[i][j+1])
            number_up   = int(grid[i+1][j])
            #print('n:',number, 'nl:',number_low,'ns:',number_side,'nu:',number_up)
            if n > number_low and n > number_l and n > number_r and n > number_up:
               x = grid[i][j]
               grid_copy[i] = grid[i].replace(x, 'X')

    return grid_copy

n = int(input())
grid = []

for _ in range(n):
    grid_item = input()
    grid.append(grid_item)

result = cavityMap(grid)
print(result)
