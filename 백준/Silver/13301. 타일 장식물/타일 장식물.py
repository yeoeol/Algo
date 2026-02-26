n = int(input())

fib = [0] * 81
fib[1] = 1
fib[2] = 1
for i in range(3, n+1):
    fib[i] = fib[i-1] + fib[i-2]

dp = [0] * 81
dp[1] = 4
# 본인*2 + (본인 + (본인-1))*2
for i in range(2, n+1):
    dp[i] = fib[i]*2 + (fib[i] + fib[i-1])*2
print(dp[n])
