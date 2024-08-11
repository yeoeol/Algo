import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y, cnt):
    global answer
    x = find(x)
    y = find(y)
    if x != y:
        if x < y:
            parent[y] = x
        else:
            parent[x] = y
    elif answer == 0:
        answer = cnt

n, m = map(int, input().split())
parent = [i for i in range(n)]

answer = 0
for i in range(m):
    a, b = map(int, input().split())
    union(a, b, i+1)

print(answer)
