n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))

stack = []
M = -1
for i in range(n):
    ind = i
    while stack and stack[-1][1] > arr[i]:
        ind, height = stack.pop()
        res = (i-ind)*height
        M = max(res, M)
    stack.append((ind, arr[i]))

while stack:
    ind, height = stack.pop()
    res = (n-ind)*height
    M = max(M, res)

print(M)