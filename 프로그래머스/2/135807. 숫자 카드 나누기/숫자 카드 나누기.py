from math import gcd
from functools import reduce

def calc(arrA, arrB):
    cd = []
    g = reduce(gcd, arrA)
    for i in range(2, g+1):
        if g % i == 0:
            cd.append(i)
            
    res = 0
    for g in cd:
        if all(num % g != 0 for num in arrB):
            res = max(res, g)
    return res

def solution(arrA, arrB):
    x = calc(arrA, arrB)
    y = calc(arrB, arrA)
    return max(x, y)
