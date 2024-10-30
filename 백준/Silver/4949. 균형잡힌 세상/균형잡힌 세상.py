import sys
input = sys.stdin.readline

while True:
    stack = []
    flag = True
    s = input().rstrip()
    if s == '.':
        break
    for i in s:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if not stack:
                flag = False
                break
            if stack[-1] == '(':
                stack.pop()
            else:
                break
        elif i == ']':
            if not stack:
                flag = False
                break
            if stack[-1] == '[':
                stack.pop()
            else:
                break
    if stack or not flag:
        print("no")
    else:
        print("yes")
