n = int(input())
cost = []

for _ in range(n):
    cost.append(int(input()))

if n == 1:
    print(cost[0])
elif n == 2:
    print(cost[1]+cost[0])
else:
    dp = [0 for _ in range(n)]

    dp[0] = cost[0]
    dp[1] = cost[0]+cost[1]
    dp[2] = max(cost[0]+cost[2], cost[1]+cost[2])

    for i in range(3, n):
        dp[i] = max(dp[i-3]+cost[i]+cost[i-1], dp[i-2]+cost[i])

    print(dp[n-1])