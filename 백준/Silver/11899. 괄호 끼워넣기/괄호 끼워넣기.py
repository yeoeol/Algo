s = input()
stack = []
answer = 0
for item in s:
    if item == '(':
        stack.append(item)
    else:
        if stack:
            stack.pop()
        else:
            answer += 1
            
print(answer+len(stack))