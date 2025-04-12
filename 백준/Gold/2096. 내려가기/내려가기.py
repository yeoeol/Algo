import sys

def input():
    return sys.stdin.readline().strip()

n = int(input())
max_dp = [[0] * 3 for _ in range(2)]
min_dp = [[0] * 3 for _ in range(2)]

# dp[i][j] ==> (i, j)의 위치에 왔을 때 얻을 수 있는 최댓값
for i in range(n):
    n1, n2, n3 = map(int, input().split())
    if i == 0:
        max_dp[0][0] = min_dp[0][0] = n1
        max_dp[0][1] = min_dp[0][1] = n2
        max_dp[0][2] = min_dp[0][2] = n3
    else:
        i %= 2
        max_dp[i][0] = max(max_dp[1-i][0], max_dp[1-i][1]) + n1
        max_dp[i][1] = max(max_dp[1-i][0], max_dp[1-i][1], max_dp[1-i][2]) + n2
        max_dp[i][2] = max(max_dp[1-i][1], max_dp[1-i][2]) + n3

        min_dp[i][0] = min(min_dp[1-i][0], min_dp[1-i][1]) + n1
        min_dp[i][1] = min(min_dp[1-i][0], min_dp[1-i][1], min_dp[1-i][2]) + n2
        min_dp[i][2] = min(min_dp[1-i][1], min_dp[1-i][2]) + n3

if n % 2 == 0:
    print(max(max_dp[1]), min(min_dp[1]))
else:
    print(max(max_dp[0]), min(min_dp[0]))
