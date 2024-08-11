def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x
        number[x] += number[y]
    print(number[x])


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


T = int(input())
for _ in range(T):
    parent, number = {}, {}

    for _ in range(int(input())):
        a, b = input().split()
        if not a in parent:
            parent[a] = a
            number[a] = 1
        if not b in parent:
            parent[b] = b
            number[b] = 1
        union(a, b)
