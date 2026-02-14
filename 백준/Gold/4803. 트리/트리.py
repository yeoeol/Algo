import sys

def input():
    return sys.stdin.readline().strip()

def dfs(graph, cur, parent, visited):
    visited[cur] = True
    for nxt in graph[cur]:
        if not visited[nxt]:
            if not dfs(graph, nxt, cur, visited):
                return False
        elif nxt != parent:
            return False
    return True

case = 1
answer = []
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    tree_cnt = 0
    visited = [False] * (n+1)
    for i in range(1, n+1):
        if not visited[i]:
            if dfs(graph, i, 0, visited):
                tree_cnt += 1

    if tree_cnt == 0:
        answer.append(f"Case {case}: No trees.")
    elif tree_cnt == 1:
        answer.append(f"Case {case}: There is one tree.")
    else:
        answer.append(f"Case {case}: A forest of {tree_cnt} trees.")
    case += 1

print(*answer, sep='\n')
