import heapq


def make_graph(n, costs):
    graph = [[0]*n for _ in range(n)]
    for a, b, c in costs:
        graph[a][b] = c
        graph[b][a] = c

    return graph


def solution(n, costs):
    graph = make_graph(n, costs)

    answer = 0
    connected = [False]*n

    queue = []
    heapq.heappush(queue, (0, costs[0][0]))
    while queue:
        wei, v = heapq.heappop(queue)
        if not connected[v]:
            connected[v] = True
            answer += wei
            for i in range(n):
                if graph[v][i] != 0 and not connected[i]:
                    heapq.heappush(queue, (graph[v][i], i))

    return answer