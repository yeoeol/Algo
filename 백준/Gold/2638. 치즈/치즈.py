from collections import deque

# 격자의 4변 중 적어도 2변 이상이 실내온도의 공기와 접촉한 것은 한 시간만에 녹음
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
# 모든 점을 순회하며 해당 위치의 값이 0이고 방문되지 않았다면 bfs 수행
# 이때 1인 위치를 만나면 next_grid에 +1
# 최종적으로 next_grid의 값을 보면서 2 이상이면 0으로 만들기

# 위 세 줄의 코드가 지나면 ans += 1


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def bfs(x, y):
    visited = [[False]*m for _ in range(n)]
    next_grid = [[0]*m for _ in range(n)]
    melt = []
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]
    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if in_range(nx, ny) and not visited[nx][ny]:
                if grid[nx][ny] == 1:
                    next_grid[nx][ny] += 1
                    if next_grid[nx][ny] >= 2:
                        melt.append((nx, ny))
                else:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    if not melt:
        return False

    for x, y in melt:
        grid[x][y] = max(0, grid[x][y]-next_grid[x][y])
    return True

ans = 0
while True:
    if not bfs(0, 0):
        print(ans)
        break
    ans += 1