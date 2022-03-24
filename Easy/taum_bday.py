#!/bin/python3

import math
import os
import random
import re
import sys

def taumBday(b, w, bc, wc, z):
    # Write your code here
    if bc > wc + z   : return (b + w)*wc + b*z 
    elif wc > bc + z : return (b + w)*bc + w*z
    return (b * bc) + (w * wc) 

if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        b = int(first_multiple_input[0])

        w = int(first_multiple_input[1])

        second_multiple_input = input().rstrip().split()

        bc = int(second_multiple_input[0])

        wc = int(second_multiple_input[1])

        z = int(second_multiple_input[2])

        result = taumBday(b, w, bc, wc, z)
        print(result)