from collections import deque

a, b, c = map(int, input().split())
visited = [[False] * (b+1) for _ in range(a+1)]
results = set()

def in_range(x, y):
    return 0 <= x <= a and 0 <= y <= b

def bfs():
    queue = deque([(0, 0)])
    visited[0][0] = True

    while queue:
        x, y = queue.popleft()
        z = c - x - y

        if x == 0:
            results.add(z)

        # a -> b
        move = min(x, b-y)
        if in_range(x-move, y+move) and not visited[x-move][y+move]:
            queue.append((x-move, y+move))
            visited[x-move][y+move] = True
        # a -> c
        move = min(x, c-z)
        if in_range(x-move, y) and not visited[x-move][y]:
            queue.append((x-move, y))
            visited[x-move][y] = True
        # b -> a
        move = min(y, a-x)
        if in_range(x+move, y-move) and not visited[x+move][y-move]:
            queue.append((x+move, y-move))
            visited[x+move][y-move] = True
        # b -> c
        move = min(y, c-z)
        if in_range(x, y-move) and not visited[x][y-move]:
            queue.append((x, y-move))
            visited[x][y-move] = True
        # c -> a
        move = min(z, a-x)
        if in_range(x+move, y) and not visited[x+move][y]:
            queue.append((x+move, y))
            visited[x+move][y] = True
        # c -> b
        move = min(z, b-y)
        if in_range(x, y+move) and not visited[x][y+move]:
            queue.append((x, y+move))
            visited[x][y+move] = True

bfs()
print(*sorted(results))