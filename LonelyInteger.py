Given an array of integers, where all elements but one occur twice, find the unique element.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    # a.sort()
    l=len(a)
    if l==1:
        return a[0]
    else:
        # for x in a:
        #     temp=0
        #     for val in a:
        #         if a[x]==a[val]:
        #             temp+=1
        #             val+=1
        #             # if x!=val:
        #             #     temp+=1
        #             #     val+=1
                    
        #     if temp==1:
        #         return a[x]
        res=a[0]
        for i  in range(1,l):
            res=res^a[i]
        return res
            
        
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
