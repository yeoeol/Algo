n = int(input())
arr = list(map(int, input().split()))

ans = [0] * n
stack = [(0, arr[0])]
for i in range(1, n):
    h = arr[i]
    while stack and stack[-1][1] < h:
        stack.pop()
    if stack:
        idx = stack[-1][0]
        ans[i] = idx+1
    stack.append((i, arr[i]))
print(*ans)