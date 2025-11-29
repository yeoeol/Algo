import sys

def input():
    return sys.stdin.readline().strip()

n, k = map(int, input().split())
values = sorted([int(input()) for _ in range(n)])

dp = [0]*(k+1) # dp[x] => x원을 만드는 경우의 수
dp[0] = 1

for value in values:
    for i in range(value, k+1):
        dp[i] += dp[i-value]

print(dp[k])