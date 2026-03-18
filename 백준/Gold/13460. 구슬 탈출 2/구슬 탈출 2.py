from collections import deque

n, m = map(int, input().split())
dxs = [0, 0, -1, 1]
dys = [-1, 1, 0, 0]

board = [list(input()) for _ in range(n)]
rx, ry = 0, 0
bx, by = 0, 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            rx, ry = i, j
        elif board[i][j] == 'B':
            bx, by = i, j

def roll(x, y, dx, dy):
    cnt = 0
    while True:
        nx, ny = x+dx, y+dy
        if board[nx][ny] == '#':
            break
        x, y = nx, ny
        cnt += 1
        if board[x][y] == 'O':
            break
    return x, y, cnt


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs():
    global rx, ry, bx, by

    visited = set()
    queue = deque()
    queue.append((rx, ry, bx, by, 0))
    visited.add((rx, ry, bx, by))

    while queue:
        rx, ry, bx, by, depth = queue.popleft()
        if depth >= 10:
            continue

        for dx, dy in zip(dxs, dys):
            nrx, nry, rc = roll(rx, ry, dx, dy)
            nbx, nby, bc = roll(bx, by, dx, dy)

            if board[nbx][nby] == 'O':
                continue

            if board[nrx][nry] == 'O':
                return depth + 1

            if nrx == nbx and nry == nby:
                if rc > bc:
                    nrx, nry = nrx-dx, nry-dy
                else:
                    nbx, nby = nbx-dx, nby-dy

            if (nrx, nry, nbx, nby) not in visited:
                visited.add((nrx, nry, nbx, nby))
                queue.append((nrx, nry, nbx, nby, depth + 1))

    return -1

print(bfs())
