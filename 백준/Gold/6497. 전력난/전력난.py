import sys
input = sys.stdin.readline

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

while True:
    m, n = map(int, input().rstrip().split())
    if m == 0 and n == 0:
        break

    city = []
    parent = [i for i in range(m)]
    total = 0

    for _ in range(n):
        x, y, z = map(int, input().rstrip().split())
        city.append((z, x, y))
        total += z
    city.sort()

    result = 0
    for w, e1, e2 in city:
        if find(e1) != find(e2):
            union(e1, e2)
            result += w
    print(total-result)