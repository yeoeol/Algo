import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, r, q = map(int, input().rstrip().split()) # 정점의 수, 루트의 번호, 쿼리의 수

graph = [[] for _ in range(n+1)]
visited = [-1 for _ in range(n+1)]

for _ in range(n-1):
    u, v = map(int, input().rstrip().split())    # 간선정보
    graph[u].append(v)
    graph[v].append(u)


def dfs(u_root):
    visited[u_root] = 1
    for i in graph[u_root]:
        if visited[i] == -1:
            visited[u_root] += dfs(i)
    return visited[u_root]

dfs(r)
for _ in range(q):
    u_root = int(input().rstrip())
    print(visited[u_root])
