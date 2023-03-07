Given a square matrix, calculate the absolute difference between the sums of its diagonals.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    
    left = 0
    right = 0;
    for i in range(0, n):
        for j in range(0, n):
 
            # Condition for principal diagonal
            if (i == j):
                left += arr[i][j]
 
            # Condition for secondary diagonal
            if ((i + j) == (n - 1)):
                right += arr[i][j]
    sum=left-right
    return abs(sum)
    
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
