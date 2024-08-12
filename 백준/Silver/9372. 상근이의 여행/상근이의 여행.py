T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    edges = []
    visited = [False] * (n+1)
    result = 0
    def so(start):
        global result
        visited[start] = True
        for i in graph[start]:
            if not visited[i]:
                result += 1
                so(i)

    so(1)
    print(result)