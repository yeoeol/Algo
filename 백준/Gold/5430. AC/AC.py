from collections import deque
import sys

input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    order = list(input().strip())
    n = int(input().strip())
    lst = input().strip('[]\n')
    if lst == '':
        lst = []
    else:
        lst = lst.split(',')

    lst = deque(lst)
    r = 0
    for o in order:
        if o == 'R':
            r += 1
        elif o == 'D':
            if lst:
                if r % 2 == 0:
                    lst.popleft()
                else:
                    lst.pop()
            else:
                print("error")
                break
    else:
        if r % 2 == 0:
            print('[', end='')
            print(*lst, sep=',', end='')
            print(']')
        else:
            lst.reverse()
            print('[', end='')
            print(*lst, sep=',', end='')
            print(']')

