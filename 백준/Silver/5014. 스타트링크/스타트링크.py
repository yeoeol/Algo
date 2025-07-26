from collections import deque

f, s, g, u, d = map(int, input().split())
if s == g:
    print(0)
    exit(0)
res = -1
queue = deque([(s, 0)])
visited = [False for _ in range(1000001)]
visited[s] = True
while queue:
    p, cnt = queue.popleft()
    if p+u == g or p-d == g:
        res = cnt+1
        break
    if p+u <= f and not visited[p+u]:
        queue.append((p+u, cnt+1))
        visited[p+u] = True
    if p-d >= 1 and not visited[p-d]:
        queue.append((p-d, cnt+1))
        visited[p-d] = True

if res == -1:
    print("use the stairs")
else:
    print(res)