import math

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


n, m = map(int, input().split())
parent = [i for i in range(n)]
path = []

for _ in range(n):
    x, y = map(int, input().split())
    path.append((x, y))

for _ in range(m):
    path_x, path_y = map(int, input().split())
    union(path_x-1, path_y-1)

edges = []
for i in range(n-1):
    for j in range(i+1, n):
        x1, y1 = path[i]
        x2, y2 = path[j]
        cost = math.sqrt(pow(x2-x1, 2)+pow(y2-y1, 2))
        edges.append((i, j, cost))
edges.sort(key=lambda x:x[2])

total = 0
for e1, e2, w in edges:
    if find(e1) != find(e2):
        union(e1, e2)
        total += w

print("%.2f"%total)