import math

def solution(n):
    num = math.sqrt(n)
    
    if str(num)[-1] == '0':
        return (num+1)**2
    
    return -1