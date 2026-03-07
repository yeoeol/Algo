n, l = map(int, input().split())
arr = sorted(map(int, input().split()))

ans = 1
num = arr[0] + (l-0.5)
for i in range(1, n):
    if arr[i] < num:
        continue
    ans += 1
    num = arr[i] + (l-0.5)
print(ans)