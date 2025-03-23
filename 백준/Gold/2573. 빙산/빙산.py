from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

ans = 0

dxs = [0, 0, 1, -1] # 동서남북
dys = [1, -1, 0, 0]
# 각 칸을 순회하면서 0이 아닌 0이 아닌 값의 위치에서
# 동서남북을 확인하여 0의 개수를 next_grid에 저장
# grid의 각 값에 next_grid 각 값을 빼기(뺸 값이 0보다 작다면 0으로 고정)
def get_zero(x, y):
    cnt = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0:
            cnt += 1
    return cnt

def simul(): # O(nm)
    melt = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] != 0:
                cnt = get_zero(i, j)
                melt.append((i, j, cnt))

    for i, j, c in melt:
        grid[i][j] = max(0, grid[i][j]-c)

# 위 과정(simul)을 한 번 수행할 때마다 bfs를 실행하여 덩어리가 분리되었는지 확인
def bfs(x, y, visited): # O(nm)
    visited[x][y] = True
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))

# 빙산이 분리되었다면 -1
# 분리되지 않았다면 0
# 모두 녹았다면 1
def check(): # O(n^2 * m^2)
    zero_flag = True

    visited = [[False]*m for _ in range(n)]
    ice_cnt = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] != 0:
                zero_flag = False
                if not visited[i][j]:
                    ice_cnt += 1
                    if ice_cnt >= 2:
                        return -1
                    bfs(i, j, visited)

    if zero_flag:
        return 1
    return 0


while True:
    simul() # O(nm)
    ans += 1

    # 빙산이 분리되었다면 -1
    # 분리되지 않았다면 0
    # 모두 녹았다면 1
    val = check() # O(n^2 * m^2)
    if val == -1:
        print(ans)
        break
    elif val == 1:
        print(0)
        break