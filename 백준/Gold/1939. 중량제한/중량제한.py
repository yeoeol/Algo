n, m = map(int, input().split())

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x, y = find(x), find(y)
    parent[x] = y

edges = [tuple(map(int, input().split())) for _ in range(m)]
edges.sort(key=lambda x:x[2], reverse=True)
x1, x2 = map(int, input().split())

left = 1
right = max(edges, key=lambda x:x[2])[2]
ans = 0
while left <= right:
    mid = (left+right)//2
    parent = [i for i in range(n+1)]

    for a, b, c in edges:
        if c >= mid:
            union(a, b)
            if find(x1) == find(x2):
                break
    if find(x1) == find(x2):
        ans = mid
        left = mid+1
    else:
        right = mid-1

print(ans)