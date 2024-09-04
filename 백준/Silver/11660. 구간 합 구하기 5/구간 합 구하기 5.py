import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
dp = [[0] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    dp[i][1] = graph[i-1][0]
    for j in range(2, n+1):
        dp[i][j] = dp[i][j-1]+graph[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().rstrip().split())

    s = 0
    for i in range(x1, x2+1):
        s += dp[i][y2]-dp[i][y1-1]
    print(s)