n = int(input())
dp = [0]*(21)
dp[1] = 1
dp[2] = 2
dp[3] = 4
dp[4] = dp[3]*2-1
dp[5] = dp[4]*2
for i in range(6, n+1):
    dp[i] = dp[i-1]*2
    if i % 2 == 0 and i >= 6:
        dp[i] -= (dp[i-5]+dp[i-4])
print(dp[n])