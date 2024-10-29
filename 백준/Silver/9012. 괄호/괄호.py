import sys
input = sys.stdin.readline

t = int(input().strip())
for i in range(t):
    stack = []
    flag = True
    ps = input().strip()
    for p in ps:
        if not stack and p == ')':
            flag = False
            break
        elif p == '(':
            stack.append(p)
        elif p == ')':
            stack.pop()
    if not flag or stack:
        print("NO")
    else:
        print("YES")