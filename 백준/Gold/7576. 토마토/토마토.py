from collections import deque

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

q = deque()
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            q.append((i, j))

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def bfs():
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            dx = cx+d[i][0]
            dy = cy+d[i][1]
            if (0 <= dx < n) and (0 <= dy < m):
                if box[dx][dy] == 0:
                    q.append((dx, dy))
                    box[dx][dy] = box[cx][cy]+1

bfs()
result = -1
for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            print(-1)
            exit(0)
        result = max(box[i][j], result)
print(result-1)
