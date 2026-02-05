import sys
sys.setrecursionlimit(10**7)

def input():
    return sys.stdin.readline().strip()

n = int(input())
arr = [0] + [int(input()) for _ in range(n)]

visited = [False]*(n+1)
path = [False]*(n+1)
ans = set()

def dfs(x):
    visited[x] = True
    path[x] = True

    nxt = arr[x]
    if not visited[nxt]:
        dfs(nxt)
    elif path[nxt]:
        cur = nxt
        while True:
            ans.add(cur)
            cur = arr[cur]
            if cur == nxt:
                break

    path[x] = False

for i in range(1, n+1):
    if not visited[i]:
        dfs(i)

ans = sorted(ans)
print(len(ans))
print(*ans, sep='\n')