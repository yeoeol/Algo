import sys
sys.setrecursionlimit(10**8)

def input():
    return sys.stdin.readline().strip()

n, m = map(int, input().split())
arr = [0]+list(map(int, input().split()))
scores = [0]*(n+1)
for _ in range(m):
    i, w = map(int, input().split())
    scores[i] += w

children = [[] for _ in range(n+1)]
for i in range(2, n+1):
    parent = arr[i]
    children[parent].append(i)

def dfs(x):
    for nxt in children[x]:
        scores[nxt] += scores[x]
        dfs(nxt)

dfs(1)
print(*scores[1:])
# 0 2 2 2 2
# 0 2 6 6 6
# 0 2 6 6 12
