#!/bin/python3

import math
import os
import random
import re
import sys

def hackerrankInString(s):
    # Write your code here
    sub = "hackerrank"
    j = 0
    for i in s:
    	if j < len(sub) and i == sub[j] : 
    		#print(j , sub[j])
    		j = j + 1

    if j == len(sub): return 'YES'
    return 'NO'



if __name__ == '__main__':
    
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)
        print(result)