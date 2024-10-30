import sys
input = sys.stdin.readline

while True:
    stack = []
    s = input().rstrip()
    if s == '.':
        break
    for i in s:
        if i == '(' or i == '[':
            stack.append(i)
        if not stack and (i == ']' or i == ')'):
            stack.append('')
            break
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                break
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                break
    if stack:
        print("no")
    else:
        print("yes")
