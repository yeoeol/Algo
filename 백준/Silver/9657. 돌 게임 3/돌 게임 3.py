n = int(input())

dp = [0] * 1001
dp[1] = True
dp[2] = False
dp[3] = True
dp[4] = True

for i in range(5, n+1):
    if not dp[i-1] or not dp[i-3] or not dp[i-4]:
        dp[i] = True
    else:
        dp[i] = False
print("SK" if dp[n] else "CY")