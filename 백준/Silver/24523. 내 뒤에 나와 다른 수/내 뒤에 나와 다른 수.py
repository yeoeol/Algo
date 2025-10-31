n = int(input())
arr = list(map(int, input().split()))
res = []
# 1 <= i < j <= n
cnt = 1
for i in range(1, n):
    if arr[i-1] != arr[i]:
        res.append((i+1, cnt))
        cnt = 1
    else:
        cnt += 1

res.append((-1, cnt))
for num, c in res:
    for _ in range(c):
        print(num, end=' ')