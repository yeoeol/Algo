import sys
from collections import deque


def in_range(x):
    return 0 <= x < 100001

def bfs(x, target):
    global answer, time

    queue = deque()
    queue.append(x)
    visited = [-1] * 100001
    visited[x] = 0

    while queue:
        x = queue.popleft()
        if visited[x] > time:
            break

        if x == target:
            time = visited[x]
            answer += 1
            continue

        for nx in [x-1, x+1, 2*x]:
            if not in_range(nx):
                continue
            if visited[nx] == -1 or visited[nx] == visited[x]+1:
                visited[nx] = visited[x]+1
                queue.append(nx)

n, k = map(int, input().split())
answer = 0
time = sys.maxsize

bfs(n, k)
print(time)
print(answer)