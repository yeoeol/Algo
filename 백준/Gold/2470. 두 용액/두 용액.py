n = int(input())
arr = sorted(list(map(int, input().split())))

i, j = 0, n-1
diff = 2000000001
left, right = arr[i], arr[j]

while i < j:
    v = arr[i]+arr[j]
    if abs(diff) > abs(v):
        left, right = arr[i], arr[j]
        diff = v

    if v > 0:
        j -= 1
    elif v < 0:
        i += 1
    else:
        break

print(left, right)