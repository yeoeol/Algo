from collections import deque

n = int(input())

def in_range(x, y):
    return 0 <= x < 1001 and 0 <= y < 1001

def bfs():
    queue = deque([(1, 0, 0)])
    visited = [[False] * 1001 for _ in range(1001)]
    visited[1][0] = True

    while queue:
        s, c, t = queue.popleft()
        if s == n:
            print(t)
            return

        if not visited[s][s]:
            visited[s][s] = True
            queue.append((s, s, t+1))
        if in_range(s+c, c) and not visited[s+c][c]:
            visited[s+c][s] = True
            queue.append((s+c, c, t+1))
        if not visited[s-1][c]:
            visited[s-1][c] = True
            queue.append((s-1, c, t+1))

bfs()