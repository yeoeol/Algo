n = int(input())
graph = [[] for _ in range(n+1)]

a, b = map(int, input().split())
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n+1)
ans = -1
def dfs(s, cnt):
    global ans
    visited[s] = True
    if s == b:
        ans = cnt
        return
    for i in graph[s]:
        if not visited[i]:
            dfs(i, cnt+1)

dfs(a, 0)
print(ans)