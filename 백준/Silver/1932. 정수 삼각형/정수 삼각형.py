n = int(input())

dp = [[0 for _ in range(n)] for _ in range(n)]
arr = []
for i in range(n):
    arr.append(tuple(map(int, input().split())))

dp[0][0] = arr[0][0]

# dp[1][0] = arr[1][0]+dp[0][0]
# dp[1][1] = arr[1][1]+dp[0][0]
#
# dp[2][0] = arr[2][0]+dp[1][0]
# dp[2][1] = arr[2][1]+max(dp[1][0], dp[1][1])
# dp[2][2] = arr[2][2]+dp[1][1]
#
# dp[3][0] = arr[3][0]+dp[2][0]
# dp[3][1] = arr[3][1]+max(dp[2][0], dp[2][1])
# dp[3][2] = arr[3][2]+max(dp[2][1], dp[2][2])
# dp[3][3] = arr[3][3]+dp[2][2]

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = arr[i][j]+dp[i-1][j]
        elif j < len(arr[i])-1:
            dp[i][j] = arr[i][j]+max(dp[i-1][j-1], dp[i-1][j])
        else:
            dp[i][j] = arr[i][j]+dp[i-1][j-1]

print(max(dp[n-1]))