#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    count = 0
    i = 0
    p = 0
    n = len(s)/3
    j = 3
    while i < n:
        x = s[p : j]
        #print(x)
        if x != 'SOS':
            k = i
            if s[p]   != 'S': count += 1
            if s[p+1] != 'O': count += 1
            if s[p+2] != 'S': count += 1
        i += 1
        p = j
        j = 3 + j
    return count

s = input()
result = marsExploration(s)
print(result)
