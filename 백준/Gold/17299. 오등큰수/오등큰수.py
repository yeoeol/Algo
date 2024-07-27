n = int(input())
arr = list(map(int, input().split()))

stack = []
F = [-1]*(max(arr)+1)
nge = [-1]*n

for i in arr:
    F[i] += 1

for i in range(len(arr)):
    while stack and F[arr[stack[-1]]] < F[arr[i]]:
        p = stack.pop()
        nge[p] = arr[i]
    stack.append(i)

print(*nge)
