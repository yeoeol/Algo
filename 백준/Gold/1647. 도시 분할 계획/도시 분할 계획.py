# n개 노드, m개 간선 무방향 가중치 그래프
# 마을을 둘로 분리하는데, 길은 최소가 되게 함 -> 가중치 최소
import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
edges = []
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    edges.append((c, a, b))
edges.sort()

parent = [i for i in range(n+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return False
    parent[y] = x
    return True

ans = 0
max_val = 0
for c, a, b in edges:
    if union(a, b):
        ans += c
        max_val = max(max_val, c)
print(ans-max_val)