from collections import deque

n = int(input())
skills = list(map(int, input().split()))

cards = deque([i for i in range(1, n+1)])
idxs = []
res = [0] * n

for skill in skills:
    if skill == 1:
        idxs.append(cards.popleft())
    elif skill == 2:
        cards.rotate(-1)
        idxs.append(cards.popleft())
        cards.rotate(1)
    elif skill == 3:
        idxs.append(cards.pop())

for idx in idxs:
    res[idx-1] = n
    n -= 1

print(*res)
