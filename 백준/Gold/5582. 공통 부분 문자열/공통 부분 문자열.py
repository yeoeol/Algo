a = input()
b = input()

dp = [0] * (len(b)+1)
res = 0

for i in range(1, len(a)+1):
    for j in range(len(b), 0, -1):
        if a[i-1] == b[j-1]:
            dp[j] = dp[j-1] + 1
            res = max(res, dp[j])
        else:
            dp[j] = 0
print(res)