import sys

def input():
    return sys.stdin.readline().strip()

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))

def dfs(s, e, visited, cnt):
    global ans

    if s == e:
        ans = cnt
        return

    for nxt, d in graph[s]:
        if not visited[nxt]:
            visited[nxt] = True
            dfs(nxt, e, visited, cnt+d)

answer = []
for _ in range(m):
    s, e = map(int, input().split())
    visited = [False] * (n+1)
    visited[s] = True

    ans = 0
    dfs(s, e, visited, 0)
    answer.append(ans)

print(*answer, sep='\n')