import sys

def input():
    return sys.stdin.readline().strip()

dic = {
    'E': (0, 1),
    'W': (0, -1),
    'S': (1, 0),
    'N': (-1, 0)
}

n, m, r = map(int, input().split())
grid = [[0] * (m+1)] + [[0]+list(map(int, input().split())) for _ in range(n)]
visited = [[False] * (m+1)] + [[False]*(m+1) for _ in range(n)]

def in_range(x, y):
    return 1 <= x <= n and 1 <= y <= m

cnt = 0
def push(grid, visited, x, y, d):
    global cnt
    cnt += 1
    dx, dy = dic[d]
    val = grid[x][y]
    visited[x][y] = True
    for i in range(1, val):
        nx, ny = x+dx*i, y+dy*i
        if not in_range(nx, ny):
            return
        if visited[nx][ny]:
            continue
        push(grid, visited, nx, ny, d)


def stand(visited, x, y):
    visited[x][y] = False

for _ in range(r):
    att_x, att_y, d = input().split()  # X행 Y열 도미노를 D방향으로 민다
    att_x, att_y = int(att_x), int(att_y)
    dep_x, dep_y = map(int, input().split())    # X행 Y열 도미노를 다시 세움

    push(grid, visited, att_x, att_y, d)
    stand(visited, dep_x, dep_y)

print(cnt)
for i in range(1, n+1):
    for j in range(1, m+1):
        print('F' if visited[i][j] else 'S', end=' ')
    print()
