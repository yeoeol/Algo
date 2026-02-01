import sys
from collections import deque

def input():
    return sys.stdin.readline().strip()

n, m = map(int, input().split())

graph = [set() for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)


def bfs(x):
    queue = deque([x])
    visited = [-1]*(n+1)
    visited[x] = 0

    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if visited[i] == -1:
                visited[i] = visited[x]+1
                queue.append(i)
    return visited[1:]


result = []
for i in range(1, n+1):
    result.append((i, sum(bfs(i))))
result.sort(key=lambda x:x[1])
print(result[0][0])