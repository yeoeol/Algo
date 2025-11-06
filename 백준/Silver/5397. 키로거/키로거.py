from collections import deque

t = int(input())
for _ in range(t):
    s = input()
    l = len(s)

    arr1 = deque()
    arr2 = deque()

    for c in s:
        if c == '<':
            if arr1:
                arr2.appendleft(arr1.pop())
        elif c == '>':
            if arr2:
                arr1.append(arr2.popleft())
        elif c == '-':
            if arr1:
                arr1.pop()
        else:
            arr1.append(c)

    print("".join(arr1+arr2))