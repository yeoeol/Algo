from collections import deque

n = int(input())
m = int(input())

queue = [tuple(map(int, input().split())) for _ in range(m)]
queue = deque(sorted(queue, key=lambda x : x[2]))

parents = [i for i in range(n+1)]
def find(x):
    if x == parents[x]:
        return parents[x]

    parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    x = find(x)
    y = find(y)

    parents[y] = x

ans = 0
while queue:
    a, b, c = queue.popleft()
    if find(a) != find(b):
        ans += c
        union(a, b)
print(ans)