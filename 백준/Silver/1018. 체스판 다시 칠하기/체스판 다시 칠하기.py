import sys
def input():
    return sys.stdin.readline().strip()

n, m = map(int, input().split())
grid = [list(input()) for _ in range(n)]

ans = 3000
color = [
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
]
def check(x, y):
    total0, total1 = 0, 0
    idx0, idx1 = 0, 1
    
    for i in range(x, x+8):
        k = 0
        idx0 = (idx0+1)%2
        idx1 = (idx1+1)%2
        for j in range(y, y+8):
            if grid[i][j] != color[idx0][k]:
                total0 += 1
            if grid[i][j] != color[idx1][k]:
                total1 += 1
            k += 1
    return min(total0, total1)

for i in range(n-7):
    for j in range(m-7):
        total = check(i, j)
        ans = min(ans, total)

print(ans)