#!/bin/python3

import math
import os
import random
import re
import sys

def palindromeIndex(s):
    # Write your code here
    n = len(s)
    f = n - 1
    index  = -1
    for i in range(n):
    	if s[i] == s[f-i] : continue
    	else              :
    		index = i
    		s1 = ''
    		for j in range(n):
    			if j != index : s1 = s1 + s[j]
    		
    		n1 = len(s1)
    		#print(s1)

    		for k in range(n1):
    			if s1[k] == s1[n1-1-k] : continue
    			else : 
    				index = -1
    				break

    		if  index == -1 :
    			index = f-i
    			s1 = ''
    			for j in range(n):
    				if j != index : s1 = s1 + s[j]
    			
    			n1 = len(s1)
    			#print(s1)
    		
    			for k in range(n1):
    				if s1[k] == s1[n1-1-k] : continue
    				else : 
    					index = -1
    					break

    			if  index == -1 : continue
    			else            : break
    		else :
    			break
    return index

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)
        print(result)
