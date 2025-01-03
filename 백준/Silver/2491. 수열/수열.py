n = int(input())
arr = list(map(int, input().split()))

dp = [1 for _ in range(n)]
dp2 = [1 for _ in range(n)]
M = m = arr[0]
for i in range(1, n):
    if arr[i] >= M:
        dp[i] += dp[i-1]
    if arr[i] <= m:
        dp2[i] += dp2[i-1]
    M = arr[i]
    m = arr[i]

print(max(max(dp), max(dp2)))
