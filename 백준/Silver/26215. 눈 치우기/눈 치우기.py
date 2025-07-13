n = int(input())
arr = list(map(int, input().split()))
if n == 1:
    ans = arr[0]
else:
    i = 0
    ans = 0
    while True:
        arr.sort(reverse=True)
        if arr[i] >= 1 and arr[i+1] >= 1:
            arr[i] -= 1
            arr[i+1] -= 1
        elif arr[i] >= 1 and arr[i+1] < 1:
            arr[i] -= 1
        else:
            break
        ans += 1
if ans > 1440:
    print(-1)
else:
    print(ans)
