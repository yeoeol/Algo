import sys
from collections import deque

input = sys.stdin.readline

d = [(0, 1), (0, -1), (1, 0), (-1, 0)] # 동서남북

# 빙산의 높이는 동서남북에 0이 저장된 칸의 개수만큼 줄어듦
n, m = map(int, input().strip().split())
iceberg = [list(map(int, input().strip().split())) for _ in range(n)]

def melt_num(iceberg, n, m):
    melt = []
    for i in range(n):
        for j in range(m):
            if iceberg[i][j] != 0:
                cnt = 0
                for dx, dy in d:
                    nx, ny = i+dx, j+dy
                    if 0 <= nx < n and 0 <= ny < m:
                        if iceberg[nx][ny] == 0:
                            cnt += 1
                melt.append((i, j, cnt))
    for i, j, cnt in melt:
        iceberg[i][j] = max(0, iceberg[i][j]-cnt)

def bfs(iceberg, x, y, visited):
    queue = deque([(x, y)])
    visited[x][y] = True
    while queue:
        px, py = queue.popleft()
        for i in range(4):
            nx, ny = px+d[i][0], py+d[i][1]
            if 0 <= nx < n and 0 <= ny < m:
                if iceberg[nx][ny] != 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

year = 0
while True:
    melt_num(iceberg, n, m)
    year += 1
    
    ice_cnt = 0 # 덩어리 수
    visited = [[False]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if iceberg[i][j] != 0 and not visited[i][j]:
                ice_cnt += 1
                bfs(iceberg, i, j, visited)

    if ice_cnt > 1:
        print(year)
        break
    
    if all(iceberg[i][j] == 0 for i in range(n) for j in range(m)):
        print(0)
        break