n = int(input())
left = list(map(int, input().split()))

result = [0 for _ in range(n)]

for i in range(1, n+1):
    cnt = 0; idx = 0
    while cnt != left[i-1]:
        if result[idx] == 0:
            cnt += 1
        idx += 1
    while result[idx] != 0:
        idx += 1
    result[idx] = i
print(*result)