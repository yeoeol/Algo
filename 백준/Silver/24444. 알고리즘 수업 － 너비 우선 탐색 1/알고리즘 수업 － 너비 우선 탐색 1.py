import sys
input = sys.stdin.readline

def bfs(start, visited):
    cnt = 1
    queue = [start]
    visited[start] = cnt
    while queue:
        p = queue.pop(0)
        for i in graph[p]:
            if visited[i] == 0:
                cnt += 1
                visited[i] = cnt
                queue.append(i)


n, m, r = map(int, input().rstrip().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(1, n+1):
    graph[i].sort()
    
visited = [0] * (n+1)
bfs(r, visited)

for i in range(1, n+1):
    print(visited[i])