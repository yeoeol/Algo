import sys
input = sys.stdin.readline

n = int(input())

arr = [int(input()) for _ in range(n)]

stack = []
result = 0

for i in range(n):
    while stack and stack[-1][1] < arr[i]:
        result += stack.pop()[0]

    if not stack:
        stack.append((1, arr[i]))
        continue

    if arr[i] == stack[-1][1]:
        cnt = stack.pop()[0]
        result += cnt

        if stack:
            result += 1
        stack.append((cnt+1, arr[i]))
    else:
        stack.append((1, arr[i]))
        result += 1

print(result)

# 1+1+2+3+4+1