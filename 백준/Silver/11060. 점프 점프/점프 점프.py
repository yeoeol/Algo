import sys

n = int(input())
arr = list(map(int, input().split()))

dp = [sys.maxsize for _ in range(n)]
dp[0] = 0

for i in range(n):
    if dp[i] != sys.maxsize:
        for j in range(1, arr[i]+1):
            next_idx = i+j
            if next_idx < n:
                dp[next_idx] = min(dp[next_idx], dp[i]+1)
                
print(dp[n-1] if dp[n-1] != sys.maxsize else -1)