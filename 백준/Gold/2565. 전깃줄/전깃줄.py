n = int(input())

arr = []
for _ in range(n):
    arr.append(tuple(map(int, input().split())))
arr.sort()

right = []
for i in range(n):
    right.append(arr[i][1])

dp = [0 for _ in range(n)]
for i in range(n):
    for j in range(i+1):
        if right[i] > right[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(n-(max(dp)+1))