import math

n = int(input())
arr = list(map(int, input().split()))

nums = list(range(1, n+1))

if arr[0] == 1:
    k = arr[1]-1
    result = []

    for i in range(n, 0, -1):
        f = math.factorial(i-1)
        idx = k // f
        k %= f
        result.append(nums[idx])
        nums.pop(idx)
    print(*result)
else:
    perm = arr[1:]
    visited = [False]*(n+1)
    answer = 0

    for i in range(n):
        cnt = 0
        for j in range(1, perm[i]):
            if not visited[j]:
                cnt += 1

        answer += cnt*math.factorial(n-i-1)
        visited[perm[i]] = True
    print(answer + 1)


