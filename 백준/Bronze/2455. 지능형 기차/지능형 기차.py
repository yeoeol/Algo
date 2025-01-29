M = -1
total = 0
for _ in range(4):
    a, b = map(int, input().split())
    M = max(M, total-a+b)
    total -= a
    total += b
print(M)