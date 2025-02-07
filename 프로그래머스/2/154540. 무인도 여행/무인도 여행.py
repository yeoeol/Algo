import sys
sys.setrecursionlimit(10**4)

def solution(maps):
    rows = len(maps)
    cols = len(maps[0])
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    def dfs(x, y):
        total = int(maps[x][y])
        visited[x][y] = True
        for dx, dy in d:
            nx, ny = x+dx, y+dy
            if 0 <= nx < rows and 0 <= ny < cols and maps[nx][ny] != 'X' and not visited[nx][ny]:
                total += dfs(nx, ny)
        return total

    result = []
    for i in range(rows):
        for j in range(cols):
            if not visited[i][j] and maps[i][j] != 'X':
                result.append(dfs(i, j))
    if not result:
        return [-1]
    return sorted(result)

