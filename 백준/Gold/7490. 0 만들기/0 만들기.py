t = int(input())

op = ['+', '-', ' ']

def calc(expr):
    total = 0
    num = 0
    sign = 1

    for ch in expr:
        if ch.isdigit():
            num = num * 10 + int(ch)
        elif ch == '+':
            total += sign * num
            num = 0
            sign = 1
        elif ch == '-':
            total += sign * num
            num = 0
            sign = -1

    total += sign * num                 # 마지막 숫자 반영
    return total

def func(idx, ops):
    global res, n
    if idx == n-1:
        expr = "1"
        for i in range(1, n):
            expr += ops[i-1]+str(i+1)
        if calc(expr.replace(" ", "")) == 0:
            res.append(expr)
        return

    for o in op:
        ops[idx] = o
        func(idx+1, ops)



ans = []
for _ in range(t):
    n = int(input())
    res = []
    ops = ['']*(n-1)
    func(0, ops)
    ans.append(res)

for a in ans:
    a.sort()
    for aa in a:
        print(aa)
    print()