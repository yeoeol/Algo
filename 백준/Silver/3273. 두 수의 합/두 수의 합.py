n = int(input())
arr = sorted(list(map(int, input().split())))
x = int(input())
res = 0
i, j = 0, n-1
while i < j:
    left = arr[i]
    right = arr[j]
    if left+right == x:
        res += 1
        i += 1
        j -= 1
    elif left+right > x:
        j -= 1
    else:
        i += 1

print(res)
