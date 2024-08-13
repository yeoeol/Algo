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

def calc(x1, y1, x2, y2):
    return round(math.sqrt((x2-x1)**2+(y2-y1)**2), 2)

n = int(input())
parent = [i for i in range(n)]
vertex = [tuple(map(float, input().split())) for _ in range(n)]
total = 0
edges = []

for i in range(n-1):
    v1 = vertex[i]
    for j in range(i+1, n):
        v2 = vertex[j]
        w = calc(v1[0], v1[1], v2[0], v2[1])
        edges.append((i, j, w))

edges.sort(key=lambda x:x[2])

for e1, e2, w in edges:
    if find(e1) != find(e2):
        total += w
        union(e1, e2)
print(total)