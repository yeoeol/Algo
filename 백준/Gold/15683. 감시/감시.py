import sys
import copy

# 방향 벡터 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# CCTV 별 감시 가능 방향
cctv_modes = {
    1: [[0], [1], [2], [3]],
    2: [[0, 1], [2, 3]],
    3: [[0, 3], [1, 3], [1, 2], [0, 2]],
    4: [[0, 2, 3], [0, 1, 3], [1, 2, 3], [0, 1, 2]],
    5: [[0, 1, 2, 3]]
}

def watch(grid, x, y, directions):
    for d in directions:
        nx, ny = x, y
        while True:
            nx += dx[d]
            ny += dy[d]
            if not (0 <= nx < N and 0 <= ny < M) or grid[nx][ny] == 6:
                break
            if grid[nx][ny] == 0:
                grid[nx][ny] = -1  # 감시 구역 표시

def count_blind_spots(grid):
    return sum(row.count(0) for row in grid)

def dfs(depth, grid):
    global min_blind_spots
    if depth == len(cctvs):
        min_blind_spots = min(min_blind_spots, count_blind_spots(grid))
        return
    
    x, y, type = cctvs[depth]
    for directions in cctv_modes[type]:
        new_grid = copy.deepcopy(grid)
        watch(new_grid, x, y, directions)
        dfs(depth + 1, new_grid)

# 입력 처리
N, M = map(int, sys.stdin.readline().split())
grid = []
cctvs = []
min_blind_spots = float('inf')

for i in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    grid.append(row)
    for j in range(M):
        if 1 <= row[j] <= 5:
            cctvs.append((i, j, row[j]))

# DFS 탐색 시작
dfs(0, grid)
print(min_blind_spots)
