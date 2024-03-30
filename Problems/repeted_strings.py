#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code here
    tam        =  len(s)
    times_in_s = s.count('a')
    x          = n % tam
    if x == 0: return n//tam * times_in_s
    new_string = s[: x]
    times_in_new_string = new_string.count('a')
    return n//tam * times_in_s + times_in_new_string

if __name__ == '__main__':

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)
    print(result)

