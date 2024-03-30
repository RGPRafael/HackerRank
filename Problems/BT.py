#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY A
#  2. INTEGER_ARRAY B
#

def beautifulPairs(A, B):
    d = dict()
    a = A.copy()
    b = B.copy()
    taken = list()
    for i in range(0, len(a)):
        chave = 0
        for j in range(0,len(b)):
            if a[i] == b[j] and j not in taken:
                d[i]  = j
                chave = 1
                taken.append(j)
                break
        if chave == 0 : d[i] = 'x'


    list_val  = list(d.values())
    indx = list_val.count('x')
    if indx == 0 : return len(d) - 1
    return len(d) - indx + 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    A = list(map(int, input().rstrip().split()))

    B = list(map(int, input().rstrip().split()))

    result = beautifulPairs(A, B)

    fptr.write(str(result) + '\n')

    fptr.close()
