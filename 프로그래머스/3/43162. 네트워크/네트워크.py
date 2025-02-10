def solution(n, computers):
    answer = 0
    def dfs(network, start, visited):
        visited[start] = True
        for i in range(n):
            if i != start and network[start][i] == 1 and not visited[i]:
                dfs(network, i, visited)

    visited = [False]*n
    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(computers, i, visited)

    return answer