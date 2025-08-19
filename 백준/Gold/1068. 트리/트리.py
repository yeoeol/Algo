n = int(input())
parent = list(map(int, input().split()))
e = int(input())

graph = [[] for _ in range(n)]
root = -1
for i, item in enumerate(parent):
    if item == -1:
        root = i
        continue
    elif i == e:
        continue
    elif item != e:
        graph[item].append(i)

def dfs(x):
    global leaf
    if not graph[x]:
        leaf += 1
    for next in graph[x]:
        if not visited[next] and next != e:
            visited[next] = True
            dfs(next)

visited = [False for _ in range(n)]
visited[root] = True
leaf = 0
if e == root:
    print(0)
else:
    dfs(root)
    print(leaf)