#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maxSubarray(arr):
    result=[]
    if max(arr) < 0:
        return [-1,-1]
    global_max, local_max = 0, 0
    for x in arr:
        local_max = max(0, local_max + x)
        global_max = max(global_max, local_max)
    result.append(global_max)
    positiv_sum=0
    for x in arr:
        if x>-1:
            positiv_sum+=x
    result.append(positiv_sum)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
