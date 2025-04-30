from collections import  deque

n = int(input())
arr = deque()

check = True
for i in range(n, 0, -1):
    if check:
        arr.appendleft(i)
        check = False
    else:
        arr.append(i)
        check = True
print(*arr)