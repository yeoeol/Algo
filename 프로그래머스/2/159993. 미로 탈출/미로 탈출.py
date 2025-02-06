from collections import deque

def find_point(maps):
    sx, sy = 0, 0
    lx, ly = 0, 0
    ex, ey = 0, 0
    for x in range(len(maps)):
        for y in range(len(maps[0])):
            if maps[x][y] == 'S':
                sx, sy = x, y
            elif maps[x][y] == 'O':
                maps[x][y] = 1
            elif maps[x][y] == 'L':
                maps[x][y] = 1
                lx, ly = x, y
            elif maps[x][y] == 'E':
                maps[x][y] = 1
                ex, ey = x, y
    return sx, sy, lx, ly, ex, ey

def bfs(maps, start_x, start_y, end_x, end_y, visited):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    maps[start_x][start_y] = 0
    visited[start_x][start_y] = True

    queue = deque([(start_x, start_y)])
    while queue:
        px, py = queue.popleft()
        for i in range(4):
            nx = px+dx[i]
            ny = py+dy[i]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    if nx == end_x and ny == end_y:
                        return maps[px][py]+1
                    if maps[nx][ny] != 'X':
                        maps[nx][ny] = maps[px][py]+1
                        queue.append((nx, ny))
    return -1

def solution(maps):
    for i in range(len(maps)):
        maps[i] = list(maps[i])
    start_x, start_y, lever_x, lever_y, end_x, end_y = find_point(maps)
    # for i in maps:
    #     print(i)
    
    visited = [[False]*len(maps[0]) for _ in range(len(maps))]
    result1 = bfs(maps, start_x, start_y, lever_x, lever_y, visited)
    if result1 == -1:
        return -1
    
    visited = [[False]*len(maps[0]) for _ in range(len(maps))]
    result2 = bfs(maps, lever_x, lever_y, end_x, end_y, visited)
    for i in maps:
        print(i)
    if result2 == -1:
        return -1

    return result1+result2