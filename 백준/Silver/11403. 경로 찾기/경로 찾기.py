import sys

sys.setrecursionlimit(10**6)

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
res = [[0] * n for _ in range(n)]

def dfs(s, e, visited):
    visited[s] = True
    for i, elem in enumerate(grid[s]):
        if i == e and elem == 1:
            return True
        if not visited[i] and elem == 1:
            if dfs(i, e, visited):
                return True

for i in range(n):
    for j in range(n):
        visited = [False for _ in range(n)]
        if dfs(i, j, visited):
            res[i][j] = 1

for r in res:
    print(*r)