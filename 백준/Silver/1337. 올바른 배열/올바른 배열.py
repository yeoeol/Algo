n = int(input())
arr = sorted([int(input()) for _ in range(n)])

min_add = 5

for i in range(n):
    cnt = 0
    for j in range(i, n):
        if arr[j] - arr[i] <= 4:
            cnt += 1
        else:
            break
    min_add = min(min_add, 5-cnt)
print(min_add)