import sys
input = sys.stdin.readline

def add(x):
    if x not in s:
        s.add(x)

def remove(x):
    if x in s:
        s.remove(x)

def check(x):
    if x in s:
        print(1)
    else:
        print(0)

def toggle(x):
    if x in s:
        remove(x)
    else:
        add(x)

def all():
    s.update(i for i in range(1, 21))

def empty():
    s.clear()

s = set()
m = int(input().rstrip())
for _ in range(m):
    o = input().rstrip().split()

    if len(o) != 1:
        op, operand = o[0], o[1]
    else:
        op = o[0]

    if op == 'add':
        add(int(operand))
    elif op == 'check':
        check(int(operand))
    elif op == 'remove':
        remove(int(operand))
    elif op == 'toggle':
        toggle(int(operand))
    elif op == 'all':
        all()
    elif op == 'empty':
        empty()
