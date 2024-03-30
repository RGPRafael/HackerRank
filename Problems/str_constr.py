#!/bin/python3

import math
import os
import random
import re
import sys
import string

#
# Complete the 'stringConstruction' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def stringConstruction(s):
    # Write your code here
    p =''
    custo = 0
    for i in s:
    	if p.count(i) == 0 : 
    	   p = p + i
    	   custo +=1
    return custo


if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = stringConstruction(s)
        print(result)

