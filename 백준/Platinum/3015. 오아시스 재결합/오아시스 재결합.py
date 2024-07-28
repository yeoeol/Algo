import sys
input = sys.stdin.readline

n = int(input())

stack = []
result = 0

for i in range(n):
    per = int(input())
    while stack and stack[-1][1] < per:
        result += stack.pop()[0]

    if not stack:
        stack.append((1, per))
        continue

    if per == stack[-1][1]:
        cnt = stack.pop()[0]
        result += cnt

        if stack:
            result += 1
        stack.append((cnt+1, per))
    else:
        stack.append((1, per))
        result += 1

print(result)

# 1+1+2+3+4+1