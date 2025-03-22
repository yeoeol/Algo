from collections import deque

n, m, t = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dxs = [0, -1, 0, 1]
dys = [1, 0, -1, 0]

# 공기청정기가 설치된 곳은 -1
# 나머지는 미세먼지의 양

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m
# 미세먼지 확산
def get_area(x, y, next_grid):
    amount = int(grid[x][y]/5) # 확산되는 양
    cnt = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if in_range(nx, ny) and grid[nx][ny] != -1:
            cnt += 1
            next_grid[nx][ny] += amount
    next_grid[x][y] -= amount*cnt

def spread():
    next_grid = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] != 0 and grid[i][j] != -1:
                get_area(i, j, next_grid) # 확산 시키기

    # 모든 칸에서 동시 확산
    for i in range(n):
        for j in range(m):
            if grid[i][j] != -1:
                grid[i][j] += next_grid[i][j]

# 공기청정기 작동
# 위쪽은 반시계, 아래쪽은 시계방향으로 순환
# 바람의 방향대로 한 칸씩 이동
# 공기청정기로 들어간 미세먼지는 모두 정화
air_cleaner = []
def get_air_cleaner():
    for i in range(n):
        for j in range(m):
            if grid[i][j] == -1:
                air_cleaner.append((i, j))


def get_arr(clock):
    arr = deque()
    if clock:
        x, y = air_cleaner[0]
        dxs = [0, -1, 0, 1]
        dys = [1, 0, -1, 0]
    else:
        x, y = air_cleaner[1]
        dxs = [0, 1, 0, -1]
        dys = [1, 0, -1, 0]

    dir_num = 0
    while True:
        dx, dy = dxs[dir_num], dys[dir_num]
        nx, ny = x+dx, y+dy
        if not in_range(nx, ny):
            dir_num = (dir_num+1) % 4
        elif grid[nx][ny] == -1:
            return arr
        else:
            arr.append(grid[nx][ny])
            x, y = nx, ny


def rotate_arr(arr):
    arr.pop()
    arr.appendleft(0)
    return arr


# 시계 방향으로 돌리기
def real_rotate(arr, clock):
    if clock:
        x, y = air_cleaner[0][0], air_cleaner[0][1]
        dxs = [0, -1, 0, 1]
        dys = [1, 0, -1, 0]
    else:
        x, y = air_cleaner[1][0], air_cleaner[1][1]
        dxs = [0, 1, 0, -1]
        dys = [1, 0, -1, 0]

    dir_num = 0
    for num in arr:
        dx, dy = dxs[dir_num], dys[dir_num]
        nx, ny = x+dx, y+dy
        if not in_range(nx, ny):
            dir_num = (dir_num+1) % 4
            dx, dy = dxs[dir_num], dys[dir_num]
            nx, ny = x+dx, y+dy
            grid[nx][ny] = num
            x, y = nx, ny
        else:
            grid[nx][ny] = num
            x, y = nx, ny


def air(): # O(n+m)
    # 위쪽(반시계로)
    arr = get_arr(True) # O(n+m)
    arr = rotate_arr(arr) # O(1)
    real_rotate(arr, True) # O(n+m)

    # 아래쪽 (시계로)
    arr2 = get_arr(False)
    arr2 = rotate_arr(arr2)
    real_rotate(arr2, False)

get_air_cleaner() # 공기 청정기 위치(한 번만 실행)
for _ in range(t):
    # 이걸 t초 반복
    spread() # O(nm)
    air() # O(n+m)

ans = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] != -1:
            ans += grid[i][j]
print(ans)


