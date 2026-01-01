n = int(input())
arr = [int(input()) for _ in range(n)]

stack = []
ans = 0

for i in range(n):
    while stack and stack[-1] <= arr[i]:
        stack.pop()
    ans += len(stack)
    stack.append(arr[i])
print(ans)