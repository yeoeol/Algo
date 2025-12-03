dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def in_range(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

def dfs(grid, x, y, visited, n, m):
    visited[x][y] = True
    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if not in_range(nx, ny, n, m):
            return True

        if grid[nx][ny] == '' and not visited[nx][ny]:
            if dfs(grid, nx, ny, visited, n, m):
                return True

    return False

def func1(grid, target):
    n, m = len(grid), len(grid[0])
    
    finds = set()
    for i in range(n):
        for j in range(m):
            if grid[i][j] == target:
                visited = [[False]*m for _ in range(n)]
                if dfs(grid, i, j, visited, n, m):
                    finds.add((i, j))

    for x, y in finds:
        grid[x][y] = ''


def func2(grid, target):
    n, m = len(grid), len(grid[0])
    for i in range(n):
        for j in range(m):
            if grid[i][j] == target:
                grid[i][j] = ''

def solution(storage, requests):
    grid = [list(s) for s in storage]
    n, m = len(grid), len(grid[0])

    for request in requests:
        if len(request) == 1:
            func1(grid, request)
        else:
            func2(grid, request[0])
        
    answer = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] != '':
                answer += 1
    return answer