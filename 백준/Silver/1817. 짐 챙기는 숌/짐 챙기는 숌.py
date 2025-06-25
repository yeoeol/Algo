n, m = map(int, input().split())
if n == 0:
    print(0)
    exit(0)

arr = list(map(int, input().split()))
cnt = 0
weight = 0
for i in range(n):
    if weight + arr[i] > m:
        cnt += 1
        weight = arr[i]
    else:
        weight += arr[i]

print(cnt+1)