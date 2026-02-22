n = int(input())

dp = [0] * 1000001
dp[2] = 1
dp[4] = 2
dp[5] = 1

for i in range(6, n+1):
    if i % 5 == 0:
        dp[i] = i // 5
    else:
        dp[i] = dp[i-2]+1

if dp[n] == 0:
    print(-1)
else:
    print(dp[n])