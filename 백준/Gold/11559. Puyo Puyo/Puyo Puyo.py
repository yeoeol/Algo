import sys
from collections import deque


def input():
    return sys.stdin.readline().strip()

def in_range(x, y):
    return 0<=x<12 and 0<=y<6

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]
grid = [list(input()) for _ in range(12)]

# 특정 뿌요 기준으로 bfs 돌리면서 개수가 4개 이상인데 더 이을 수 없다면
def bfs(x, y, grid, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    color = grid[x][y]

    group = [(x, y)]

    while queue:
        x, y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if in_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] == color:
                visited[nx][ny] = True
                queue.append((nx, ny))
                group.append((nx, ny))

    return group

res = 0
while True:
    # 터뜨릴 것들 탐색
    visited = [[False]*6 for _ in range(12)]
    groups = []
    for i in range(12):
        for j in range(6):
            if grid[i][j] != '.' and not visited[i][j]:
                group = bfs(i, j, grid, visited)
                if len(group) >= 4:
                    groups.extend(group)
    if not groups:
        break
    # 터뜨리기
    for x, y in groups:
        grid[x][y] = '.'

    # 중력
    def find_puyo_by_col(y):
        lst = []
        for i in range(12):
            if grid[i][y] != '.':
                lst.append(grid[i][y])
                grid[i][y] = '.'
        return lst

    for j in range(6):
        lst = find_puyo_by_col(j)
        for i in range(11, -1, -1):
            if lst and grid[i][j] == '.':
                grid[i][j] = lst.pop()
    res += 1

print(res)