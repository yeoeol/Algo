from collections import deque

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    res = 0

    while queue:
        M = max(queue)

        front = queue.popleft()
        m -= 1

        if M == front:
            res += 1
            if m < 0:
                print(res)
                break
        else:
            queue.append(front)
            if m < 0:
                m = len(queue)-1
