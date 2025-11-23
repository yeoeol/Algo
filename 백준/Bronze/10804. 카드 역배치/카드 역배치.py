arr = list(range(21))
for _ in range(10):
    a, b = map(int, input().split())
    arr[a:b+1] = arr[a:b+1][::-1]

print(*arr[1:])
