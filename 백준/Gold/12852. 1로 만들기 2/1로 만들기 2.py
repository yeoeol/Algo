from collections import deque


def bfs(x):
    visited = [False]*(x+1)
    visited[x] = True
    queue = deque()
    queue.append((x, [x]))

    while queue:
        p, lst = queue.popleft()
        if p == 1:
            return lst

        if p % 3 == 0 and not visited[p//3]:
            queue.append((p//3, lst+[p//3]))
            visited[p//3] = True
        if p % 2 == 0 and not visited[p//2]:
            queue.append((p//2, lst+[p//2]))
            visited[p//2] = True
        if not visited[p-1]:
            queue.append((p-1, lst+[p-1]))
            visited[p-1] = True

n = int(input())
arr = bfs(n)
print(len(arr)-1)
print(*arr)