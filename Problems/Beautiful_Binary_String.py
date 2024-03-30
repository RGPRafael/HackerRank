#!/bin/python3

import math
import os
import random
import re
import sys

def beautifulBinaryString(b):
	i = b.find('010') #finds the begining
	if i == -1 : return 0
	changes = 0
	while( i != -1 ): #find something
		#print(i)
		new_list = list()
		for j in b : new_list.append(j) 
		new_list[i+2] = '1'
		#print(new_list)
		changes = changes + 1
		b = ''.join(new_list)
		i = b.find('010')
	return changes

if __name__ == '__main__':
   
    b = input()
    result = beautifulBinaryString(b)
    print (result)