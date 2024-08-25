n, s = map(int, input().split())
arr = list(map(int, input().split()))

m = n+1
i, j = 0, 0
_sum = 0

while True:
    if _sum >= s:
        m = min(m, j-i)
        _sum -= arr[i]
        i += 1
    elif j == n:
        break
    else:
        _sum += arr[j]
        j += 1

if m == n+1:
    print(0)
else:
    print(m)