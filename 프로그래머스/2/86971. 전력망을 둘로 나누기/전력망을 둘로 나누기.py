import sys

def make_graph(n, edges):
    graph = [[] for _ in range(n+1)]
    for e1, e2 in edges:
        graph[e1].append(e2)
        graph[e2].append(e1)
    return graph

def dfs(graph, s, visited):
    visited[s] = True
    cnt = 1
    for w in graph[s]:
        if not visited[w]:
            cnt += dfs(graph, w, visited)
    return cnt
def solution(n, wires):
    answer = -1
    m = sys.maxsize
    original_wires = wires.copy()

    for i in range(n-1):
        w1, w2 = wires.pop(i)
        graph = make_graph(n, wires)

        visited1 = [False]*(n+1)
        d1 = dfs(graph, w1, visited1)
        d2 = dfs(graph, w2, visited1)

        m = min(m, abs(d1-d2))

        wires = original_wires.copy()
        
    return m