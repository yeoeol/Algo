n = int(input())
arr = list(map(int, input().split()))

dp1 = [0 for _ in range(n)]
dp2 = [0 for _ in range(n)]


for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp1[i] = max(dp1[i], dp1[j]+1)

arr_reverse = arr[::-1]
for i in range(1, n):
    for j in range(i):
        if arr_reverse[j] < arr_reverse[i]:
            dp2[i] = max(dp2[i], dp2[j]+1)
dp2 = dp2[::-1]

answer = 0
for i in range(n):
    answer = max(answer, dp1[i]+dp2[i])

print(answer+1)