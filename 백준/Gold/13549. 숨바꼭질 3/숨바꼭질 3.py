from collections import deque

n, k = map(int, input().split())

visited = [-1] * 100001
def bfs(start):
    queue = deque([start])
    visited[start] = 0

    while queue:
        p = queue.popleft()
        if p == k:
            print(visited[p])
            return
        for i in [p-1, p+1, 2*p]:
            if 0 <= i <= 100000 and visited[i] == -1:
                if i == 2*p:
                    visited[i] = visited[p]
                    queue.appendleft(i)
                else:
                    visited[i] = visited[p]+1
                    queue.append(i)
bfs(n)
