n = int(input())
dp = [0]+[50001 for _ in range(n)]

for i in range(1, n+1):
    j = 1
    while j*j <= i:
        dp[i] = min(dp[i-j*j]+1, dp[i])
        j += 1

print(dp[n])