import sys
input = sys.stdin.readline

stack = []
def one(x):
    stack.append(x)

def two():
    if stack:
        print(stack.pop())
    else:
        print(-1)

def three():
    print(len(stack))

def four():
    if stack:
        print(0)
    else:
        print(1)

def five():
    if stack:
        print(stack[-1])
    else:
        print(-1)

n = int(input().strip())
for i in range(n):
    order = list(map(int, input().strip().split()))
    if order[0] == 1:
        one(order[1])
    elif order[0] == 2:
        two()
    elif order[0] == 3:
        three()
    elif order[0] == 4:
        four()
    else:
        five()