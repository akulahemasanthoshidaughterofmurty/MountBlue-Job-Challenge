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
    i=j=0
    total=sum1=0
    while(i<len(arr)):
        sum1+=arr[i][j] 
        i+=1
        j+=1
    
    i=0
    j=len(arr)-1
    while(i<len(arr)):
        total+=arr[i][j]
        i+=1
        j-=1
    res=sum1-total
   
    return abs(res)
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
