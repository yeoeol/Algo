import sys


def input():
    return sys.stdin.readline().strip()

n = int(input())
visited = [False] * 200001
ans = 0
for _ in range(n):
    a, b = map(int, input().split())
    if b == 1:
        if not visited[a]:
            visited[a] = True
        else:
            ans += 1
    else:
        if not visited[a]:
            ans += 1
        else:
            visited[a] = False
ans += visited.count(True)
print(ans)