from collections import deque

n = int(input())
space = []
for _ in range(n):
    space.append(list(map(int, input().split())))

fishes = []
x, y = 0, 0
for i in range(n):
    for j in range(n):
        if space[i][j] == 9:
            x, y = i, j
        elif space[i][j] != 0:
            fishes.append((i, j))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, baby_size):
    graph = [[0]*n for _ in range(n)]
    visited = [[False]*n for _ in range(n)]
    queue = deque([(x, y)])
    while queue:
        px, py = queue.popleft()
        visited[px][py] = True
        for i in range(4):
            nx = px+dx[i]
            ny = py+dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if baby_size < space[nx][ny]:
                    continue
                else:
                    if graph[nx][ny] == 0 and not visited[nx][ny]:
                        graph[nx][ny] = graph[px][py]+1
                        queue.append((nx, ny))
    return graph

time = 0
baby_shark_size = 2
eat_fish = 0

while fishes:
    dist = bfs(x, y, baby_shark_size)
    fishes.sort(key=lambda x: (dist[x[0]][x[1]], x[0], x[1]))
    # print(x, y)
    # for d in dist: print(d)
    # print(fishes)
    # print('--------------------')
    for i in range(len(fishes)):
        fx, fy = fishes[i][0], fishes[i][1]
        if dist[fx][fy] != 0 and space[fx][fy] < baby_shark_size:
            time += dist[fx][fy]
            space[x][y] = 0
            space[fx][fy] = 0
            eat_fish += 1
            if eat_fish == baby_shark_size:
                eat_fish = 0
                baby_shark_size += 1
            x, y = fx, fy
            fishes.pop(i)
            break
    else:
        break
print(time)