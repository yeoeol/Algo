from collections import deque

n = int(input())
arr = list(map(int, input().split()))

visited = [-1 for _ in range(n)]
def bfs():
    queue = deque()
    queue.append(0)
    visited[0] = 0

    while queue:
        idx = queue.popleft()

        for i in range(1, arr[idx]+1):
            next_idx = idx+i
            if next_idx < n and visited[next_idx] == -1:
                queue.append(next_idx)
                visited[next_idx] = visited[idx]+1

bfs()
print(visited[n-1])
