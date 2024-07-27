s = input()
bomb = list(input())

stack = []
for i in range(len(s)):
    stack.append(s[i])
    if bomb[-1] == stack[-1]:
        if stack[-1:-1-len(bomb):-1] == bomb[-1::-1]:
            for _ in range(len(bomb)):
                stack.pop()

if len(stack) == 0:
    print("FRULA")
else:
    print(''.join(stack))