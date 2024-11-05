n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

dp = [[0]*(m+1) for _ in range(n+1)]
for i in range(1, n+1):
    dp[i][1] = arr[i-1][0]
    for j in range(2, m+1):
        dp[i][j] = dp[i][j-1] + arr[i-1][j-1]


k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    _sum = 0
    for d in range(i, x+1):
        _sum += dp[d][y]-dp[d][j-1]
    print(_sum)