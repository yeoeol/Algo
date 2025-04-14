n, s = map(int, input().split())
arr = list(map(int, input().split()))

total = 0
ans = 0
lst = []
def rec(start, cnt, max_cnt):
    global ans, total
    if cnt == max_cnt:
        if total == s:
            ans += 1
        return

    for i in range(start, n):
        total += arr[i]
        rec(i+1, cnt+1, max_cnt)
        total -= arr[i]

for i in range(1, n+1):
    rec(0, 0, i)
print(ans)