import sys
sys.setrecursionlimit(10**8)

def input():
    return sys.stdin.readline().strip()


n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

def rec(x, y, l):
    if l == 2:
        return sorted([grid[x][y], grid[x][y+1], grid[x+1][y], grid[x+1][y+1]])[1]

    return sorted([
        rec(x, y, l//2),
        rec(x, y+l//2, l//2),
        rec(x+l//2, y, l//2),
        rec(x+l//2, y+l//2, l//2)
    ])[1]

if n == 1:
    print(grid[0][0])
else:
    print(rec(0, 0, n))