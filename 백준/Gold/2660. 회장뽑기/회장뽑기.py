import sys
from collections import deque

n = int(input())
a, b = map(int, input().split())

graph = [[] for _ in range(n+1)]
while (a, b) != (-1, -1):
    graph[a].append(b)
    graph[b].append(a)

    a, b = map(int, input().split())

def bfs(x):
    visited = [False]*(n+1)
    visited[x] = True
    queue = deque()
    queue.append(x)

    dist = [0] * (n+1)
    while queue:
        p = queue.popleft()
        for e in graph[p]:
            if not visited[e]:
                visited[e] = True
                queue.append(e)
                dist[e] = dist[p]+1
    return max(dist)

score = [sys.maxsize]
for i in range(1, n+1):
    score.append(bfs(i))

m = min(score)
ans = []
for i, num in enumerate(score):
    if num == m:
        ans.append(i)

print(m, len(ans))
print(*ans)