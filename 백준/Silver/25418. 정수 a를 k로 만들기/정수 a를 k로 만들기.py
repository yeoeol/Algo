from collections import deque

a, k = map(int, input().split())

def bfs(x):
    visited = [False] * (k+2)
    queue = deque()
    queue.append((x, 0))
    visited[x] = True
    while queue:
        x, cnt = queue.popleft()
        if x == k:
            return cnt

        for nx in [x+1, x*2]:
            if nx <= k and not visited[nx]:
                visited[nx] = True
                queue.append((nx, cnt+1))

print(bfs(a))