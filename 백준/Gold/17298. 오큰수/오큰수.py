from sys import stdin

n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))

stack = []
result = [-1] * n

for i in range(n):
    while stack and a[i] > a[stack[-1]]:
        result[stack.pop()] = a[i]
    stack.append(i)
print(*(result))
