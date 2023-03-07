Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
        
        
        #!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    for x in s:
        if "P" in s:
            c1=s[0:2] ##hours
            c2=s[2:-2] ##without pm           
            c=int(c1)
            if c==12:
                return s[0:-2]
            else:            
             c+=12
             st=str(c)            
             ans=st+c2            
             return ans       
                        
        if "A" in s:
         a2=s[2:-2]        
         a1=s[0:2] 
         ##hours
         hou=int(a1)
         if hou==12:
             hou-=12             
             a=str(hou)
             z="0"             
             res1=z+a+a2
             
             return res1             
         else:
           res=s[0:-2]
           print(res)
           return res
                 
             
         
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
