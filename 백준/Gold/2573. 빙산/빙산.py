import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

d = [(0, 1), (0, -1), (1, 0), (-1, 0)] # 동서남북

# 빙산의 높이는 동서남북에 0이 저장된 칸의 개수만큼 줄어듦
n, m = map(int, input().strip().split())
iceberg = [list(map(int, input().strip().split())) for _ in range(n)]

year = 0
while True:
    melt = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if iceberg[i][j] != 0:
                cnt = 0
                for dx, dy in d:
                    nx, ny = i+dx, j+dy
                    if 0 <= nx < n and 0 <= ny < m:
                        if iceberg[nx][ny] == 0:
                            cnt += 1
                melt[i][j] = cnt

    for i in range(n):
        for j in range(m):
            if iceberg[i][j] != 0:
                iceberg[i][j] = max(0, iceberg[i][j]-melt[i][j])
    year += 1

    def dfs(iceberg, x, y, visited):
        visited[x][y] = True
        for i in range(4):
            nx, ny = x+d[i][0], y+d[i][1]
            if 0 <= nx < n and 0 <= ny < m:
                if iceberg[nx][ny] != 0 and not visited[nx][ny]:
                    dfs(iceberg, nx, ny, visited)

    def check(iceberg, n, m):
        visited = [[False]*m for _ in range(n)]
        flag = False
        for i in range(n):
            for j in range(m):
                if iceberg[i][j] != 0 and not visited[i][j]:
                    if flag:
                        return True
                    flag = True
                    dfs(iceberg, i, j, visited)
        return False

    if all(iceberg[i][j] == 0 for i in range(n) for j in range(m)):
        print(0)
        break

    if check(iceberg, n, m):
        print(year)
        break
