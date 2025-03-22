from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 치즈 총 개수 구해놓고 녹은 개수 계산해서 빼주기
# 덩어리 중에 가장 바깥에 있는(공기와 접촉된) 것들은 녹음

# 결국 치즈 덩어리의 가장자리를 구하는 것이 중요한 문제
# 외부 공기를 bfs로 탐색(0 인거 queue에 집어넣기), grid[x][y]가 1인 부분은 next_grid[x][y] 도 1로 만들기
# visited 배열 만들어서 관리
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def melt(grid, melt_grid):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if melt_grid[i][j]:
                cnt += 1
                grid[i][j] = 0
    return cnt

def bfs(x, y, n, m):
    melt_grid = [[False]*m for _ in range(n)]
    visited = [[False]*m for _ in range(n)]

    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if in_range(nx, ny) and not visited[nx][ny]:
                if grid[nx][ny] == 0:
                    queue.append((nx, ny))
                else:
                    melt_grid[nx][ny] = True

                visited[nx][ny] = True


    cnt = melt(grid, melt_grid)
    return cnt


def get_total_cheese():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                cnt += 1
    return cnt

cnt = get_total_cheese() # 총 치즈 개수 구하기(한 번만 실행)
t = 0
while True:
    melt_cnt = bfs(0, 0, n, m)
    t += 1
    if cnt-melt_cnt == 0:
        print(t)
        print(cnt)
        break
    cnt -= melt_cnt

