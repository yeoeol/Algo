import sys
from copy import copy

sys.setrecursionlimit(10**7)

def make_graph(edges, n):
    graph = [[] for _ in range(n+1)]
    for a, b, c in edges:
        graph[a].append((b, c))
        graph[b].append((a, c))
    return graph

answer = 0
def solution(n, infection, edges, k):
    global answer
    answer = 0

    graph = make_graph(edges, n)
    infected = [False]*(n+1)
    infected[infection] = True
    dfs_pipe_sequence(graph, 0, infected, k)

    return answer

def count(arr):
    return arr.count(True)

def dfs_same_pipe(graph, x, infected, pipe):
    for nxt, nxt_pipe in graph[x]:
        if pipe == nxt_pipe and not infected[nxt]:
            infected[nxt] = True
            dfs_same_pipe(graph, nxt, infected, pipe)

def spread_by_pipe(graph, infected, pipe):
    for node in range(1, len(infected)):
        if infected[node]:
            dfs_same_pipe(graph, node, infected, pipe)
            
def dfs_pipe_sequence(graph, depth, infected, k):
    global answer

    answer = max(answer, count(infected))

    if depth == k:
        return

    for pipe in [1,2,3]:
        next_infected = copy(infected)
        spread_by_pipe(graph, next_infected, pipe)
        dfs_pipe_sequence(graph, depth+1, next_infected, k)