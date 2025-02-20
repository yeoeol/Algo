from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)

    tickets.sort()

    for a, b in tickets:
        graph[a].append(b)

    visited = []

    def dfs(cur):
        while graph[cur]:
            next = graph[cur].pop(0)
            dfs(next)
        visited.append(cur)

    dfs("ICN")
    return visited[::-1]