T = int(input())

def so(start, cnt):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            cnt = so(i, cnt+1)
    return cnt

for _ in range(T):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (n+1)
    c = so(1, 0)
    print(c)