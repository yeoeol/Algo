grid = [[0] * 101 for i in range(101)]

n, m = map(int, input().split())
for _ in range(n):
    a, b, c, d = map(int, input().split())
    for i in range(a, c+1):
        for j in range(b, d+1):
            grid[i][j] += 1

ans = 0
for i in range(101):
    for j in range(101):
        if grid[i][j] > m:
            ans += 1
print(ans)