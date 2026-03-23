t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    res = 0
    max_num = arr[n-1]
    for i in range(n-2, -1, -1):
        if arr[i] < max_num:
            res += max_num-arr[i]
        else:
            max_num = arr[i]
    ans.append(res)

print(*ans, sep='\n')