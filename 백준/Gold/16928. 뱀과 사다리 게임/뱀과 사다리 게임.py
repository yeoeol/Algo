from collections import deque

n, m = map(int, input().split())

board = [0] * 101
visited = [False] * 101

up = dict()
down = dict()
for _ in range(n):
    x, y = map(int, input().split())
    up[x] = y
for _ in range(m):
    u, v = map(int, input().split())
    down[u] = v

def bfs():
    q = deque([1])
    visited[1] = True
    while q:
        p = q.popleft()
        if p == 100:
            print(board[100])
            break
        for i in range(1, 7):
            next = p+i
            if 1 <= next <= 100 and not visited[next]:
                if next in up.keys():
                    next = up[next]
                if next in down.keys():
                    next = down[next]
                if not visited[next]:
                    visited[next] = True
                    board[next] = board[p]+1
                    q.append(next)

bfs()