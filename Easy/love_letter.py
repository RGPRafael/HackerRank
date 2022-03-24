#!/bin/python3

import math
import os
import random
import re
import sys


def theLoveLetterMystery(s):
    # Write your code here
    alphabet    = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
    list_aphabet = alphabet.split()
    n = len(s)
    if n % 2 == 0 : n = n//2  
    else          : n = n//2 + 1 
    op = 0
    for i in range(n):
    	if s[i] != s[len(s) - 1 - i] : 
    		pos_f = list_aphabet.index(s[len(s) - 1 - i])
    		pos_i = list_aphabet.index(s[i])
    		if pos_f > pos_i : op = pos_f - pos_i  + op
    		else             : op = pos_i - pos_f  + op
    return op




if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        s = input()
        result = theLoveLetterMystery(s)
        print(result)