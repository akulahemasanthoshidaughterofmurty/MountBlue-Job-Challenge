#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    def maximum(l,n):
        res=l[0]
        maxcount=0
        for i in range(1,n):
            if(res<l[i]):
                res=l[i]
                maxcount+=1
        return maxcount


    def minimum(l,n):
        res=l[0]
        mincount=0
        for i in range(1,n):
            if(res>l[i]):
                res=l[i]
                mincount+=1
        return mincount
    l=scores
    n=len(l)
    res1=maximum(l,n)
    res2=minimum(l,n)
    result=[]
    result.append(res1)
    result.append(res2)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
