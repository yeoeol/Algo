from collections import deque

def in_range(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

def bfs(maps):
    n = len(maps)
    m = len(maps[0])
    
    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]
    visited = [[False]*m for _ in range(n)]
    
    visited[0][0] = True
    queue = deque([(0, 0, 1)])
    
    while queue:
        x, y, s = queue.popleft()
        if x == n-1 and y == m-1:
            return s
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if in_range(nx, ny, n, m) and maps[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, s+1))
    return -1

def solution(maps):
    step = bfs(maps)
    return -1 if step == -1 else step
