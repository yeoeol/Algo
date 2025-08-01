from collections import deque


n, m = map(int, input().split())
positions = list(map(int, input().split()))

cnt = 0
queue = deque([i for i in range(1, n + 1)])
for pos in positions:
    idx = queue.index(pos)
    if idx <= len(queue) // 2:
        queue.rotate(-idx)
        queue.popleft()
        cnt += idx
    else:
        num = len(queue)-idx
        queue.rotate(num)
        queue.popleft()
        cnt += num

print(cnt)