#!/bin/python3

import math
import os
import random
import re
import sys
import string

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    string_alphabet   = string. ascii_lowercase
    s_copy            = s.replace(' ','').casefold()
    conjunto_alphabet = set()
    conjunto_s        = set()

    #print(string_alphabet)
    #print(s_copy)

    for i in string_alphabet : conjunto_alphabet.add(i)
    for j in s_copy : conjunto_s.add(j)

    #print(conjunto_alphabet)
    #print(conjunto_s)

    x = conjunto_s.symmetric_difference(conjunto_alphabet)
    #print(x)
    if len(x) == 0 : return 'pangram'
    return 'not pangram'



if __name__ == '__main__':

    s = input()
    result = pangrams(s)
    print(result)