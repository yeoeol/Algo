import sys
from collections import deque


def input():
    return sys.stdin.readline().strip()

n = int(input())
s = deque()
orders = []

def append_end(block):
    global s
    s.append(block)

def append_front(block):
    global s
    s.appendleft(block)

def delete():
    global s
    if len(s) == 0:
        return
    o = orders.pop()
    if o == '1':
        s.pop()
    else:
        s.popleft()

for _ in range(n):
    split = input().split()
    if split[0] == '3':
        delete()
    else:
        order, block = split[0], split[1]
        if order == '1':
            orders.append(order)
            append_end(block)
        else:
            orders.append(order)
            append_front(block)

print(''.join(s) if len(s) != 0 else 0)
