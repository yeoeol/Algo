import sys

def input(): return sys.stdin.readline().strip()

t = int(input())
for _ in range(t):
    k = int(input())
    arr = [0]+list(map(int, input().split()))

    prefix_sum = [0] * (k+1)
    for i in range(1, k+1):
        prefix_sum[i] = prefix_sum[i-1] + arr[i]

    dp = [[0] * (k+1) for _ in range(k+1)]
    for length in range(1, k+1):
        for start in range(1, k-length+1):
            end = start+length

            MIN = sys.maxsize
            for mid in range(start, end):
                MIN = min(MIN, dp[start][mid] + dp[mid+1][end])

            dp[start][end] = MIN + prefix_sum[end] - prefix_sum[start-1]

    print(dp[1][-1])