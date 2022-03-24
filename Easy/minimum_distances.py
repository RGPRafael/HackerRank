#!/bin/python3

# Complete the minimumDistances function below.
def minimumDistances(a):
    min = None
    i   =  0
    sorted_list = sorted( a )
    #print( sorted_list )
    repeat_values = list( )
    while( i < len( sorted_list ) ) :
        x = sorted_list[ i ]
        count = a.count( x )
        if count != 1:
                 repeat_values.append( x )
                 i = i + 2
        else :   i = i + 1

    #print(repeat_values)
    if len(repeat_values) ==  0 : return -1
    for j in repeat_values :
        x = a.index(j)
        y = a.index(j,x+1)
        if   min == None  : min = y - x
        elif min  > y - x : min = y - x
        #print(y - x)

    return min

n = int(input())
a = list(map(int, input().rstrip().split()))
result = minimumDistances(a)
print(result)
