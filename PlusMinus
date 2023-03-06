#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    z,n,p=0,0,0

    for x in arr:
        if x==0:
            z+=1
        elif x<0:
            n+=1
        else:
            p+=1
    
    plus=[p/len(arr),n/len(arr),z/len(arr)] 
    for x in plus:
        print('%6f'%x) 
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
