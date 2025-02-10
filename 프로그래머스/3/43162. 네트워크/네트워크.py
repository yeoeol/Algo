def solution(n, computers):
    answer = 0
    net = [[] for _ in range(n+1)]

    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                net[i+1].append(j+1)

    def dfs(network, start, visited):
        visited[start] = True
        for n in network[start]:
            if not visited[n]:
                dfs(network, n, visited)

    visited = [False]*(n+1)
    for i in range(1, n+1):
        if not visited[i]:
            answer += 1
            dfs(net, i, visited)

    return answer