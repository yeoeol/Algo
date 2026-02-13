import sys

def input():
    return sys.stdin.readline().strip()

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))

def dfs(s, e, visited):
    if s == e:
        return 0

    for nxt, d in graph[s]:
        if not visited[nxt]:
            visited[nxt] = True
            result = dfs(nxt, e, visited)
            if result is not None:
                return result + d
    
    return None

answer = []
for _ in range(m):
    s, e = map(int, input().split())
    visited = [False] * (n+1)
    visited[s] = True

    answer.append(dfs(s, e, visited))

print(*answer, sep='\n')