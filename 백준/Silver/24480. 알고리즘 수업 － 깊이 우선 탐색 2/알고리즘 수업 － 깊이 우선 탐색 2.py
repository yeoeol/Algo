import sys
sys.setrecursionlimit(150000)
input = sys.stdin.readline

n, m, r = map(int, input().rstrip().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n+1):
    graph[i].sort(reverse=True)
# print(graph)

cnt = 1
visited = [0] * (n+1)
def dfs(start):
    global cnt
    visited[start] = cnt

    for i in graph[start]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)

dfs(r)
for i in range(1, n+1):
    print(visited[i])