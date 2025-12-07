from collections import deque, defaultdict

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def bfs(land, x, y, visited, dic, idx):
    n, m = len(land), len(land[0])
    visited[x][y] = True
    queue = deque()
    queue.append((x, y))

    c = [(x, y)]
    dic[idx].add((x, y))
    land[x][y] = idx
    while queue:
        x, y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and land[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))
                land[nx][ny] = idx
                dic[idx].add((nx, ny))


def solution(land):
    n, m = len(land), len(land[0])
    visited = [[False]*m for _ in range(n)]
    
    dic = defaultdict(set)
    idx = 1
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                bfs(land, i, j, visited, dic, idx)
                idx += 1
    res = 0
    for j in range(m):
        arr = set()
        for i in range(n):
            if land[i][j] != 0 and land[i][j] not in arr:
                arr.add(land[i][j])
        cnt = 0
        for s in arr:
            cnt += len(dic[s])
        res = max(res, cnt)
        
    return res
