import sys

def solution(arr):
    n = len(arr)
    arr = [0] + arr
    
    # 1. 처음 집 포함, 마지막집 제외시 최적 (인덱스 1~n-1)
    
    dp1 = [0] * (n+1)
    dp1[1] = arr[1]
    dp1[2] = max(dp1[1], arr[2])
    for i in range(3, n+1):
        dp1[i] = max(dp1[i-1], dp1[i-2]+arr[i])
    
    # 2. 처음 집 제외, 마지막집 포함시 최적 (인덱스 2~n)
    dp2 = [0] * (n+1)
    dp2[1] = 0
    dp2[2] = arr[2]
    for i in range(3, n+1):
        dp2[i] = max(dp2[i-1], dp2[i-2]+arr[i])
        
    return max(dp1[n-1], dp2[n])
