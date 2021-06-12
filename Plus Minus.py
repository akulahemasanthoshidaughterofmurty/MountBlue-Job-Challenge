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
    # Write your code here
    zero=neg=pos=0
    for i in arr:
        if(i==0):
            zero+=1
        elif(i<0):
            neg+=1
        else:
            pos+=1
    n=len(arr)
    print("{:.6f}".format(pos/n))    #this fromat used to place the decimals upto fixed format
    print("{:.6f}".format(neg/n))
    print("{:.6f}".format(zero/n))
   
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
