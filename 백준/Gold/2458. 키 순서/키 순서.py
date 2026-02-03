import sys

def input():
    return sys.stdin.readline().strip()

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
re_graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    re_graph[b].append(a)

def dfs(g, start, sets, visited):
    visited[start] = True
    for nxt in g[start]:
        if not visited[nxt]:
            sets.add(nxt)
            dfs(g, nxt, sets, visited)

answer = 0
for i in range(1, n+1):
    sets = set()
    visited = [False]*(n+1)
    dfs(graph, i, sets, visited)

    visited = [False]*(n+1)
    dfs(re_graph, i, sets, visited)
    if len(sets) == n-1:
        answer += 1

print(answer)