n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
moves = [list(map(int, input().split())) for _ in range(m)]

dxs = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dys = [0, -1, -1, 0, 1, 1, 1, 0, -1]

clouds = [[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]]

def move_cloud(cs, d, s):
    dx, dy = dxs[d]*s, dys[d]*s
    for i in range(len(cs)):
        x, y = cs[i]
        x, y = (x+dx)%n, (y+dy)%n
        cs[i] = [x, y]


def increase_water(cs):
    for x, y in cs:
        grid[x][y] += 1


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def water_bug(cs):
    arr = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
    for x, y in cs:
        cnt = 0
        for dx, dy in arr:
            nx, ny = x+dx, y+dy
            if in_range(nx, ny) and grid[nx][ny] > 0:
                cnt += 1
        if cnt > 0:
            grid[x][y] += cnt


def make_cloud(cs):
    old_cloud_set = set(tuple(c) for c in cs)

    new_clouds = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] >= 2 and (i, j) not in old_cloud_set:
                new_clouds.append([i, j])
                grid[i][j] -= 2
    cs.clear()
    cs.extend(new_clouds)

for d, s in moves:
    move_cloud(clouds, d, s)    # 모든 구름이 d 방향으로 s칸 이동
    increase_water(clouds)      # 물의 양 1 증가
    water_bug(clouds)           # 물복사버그 마법 시전

    make_cloud(clouds)          # 물의 양이 2 이상인 모든 칸에 구름 생성, 물의 양 2 제거
                                # 구름이 생기는 칸은 위에서 사라진 칸이 아니어야 함

answer = 0
for g in grid:
    answer += sum(g)
print(answer)