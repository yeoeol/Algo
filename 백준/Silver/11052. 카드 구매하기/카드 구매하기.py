n = int(input())
prices = [0]+list(map(int, input().split()))

# dp[i] = 카드 i개를 구매할 때 얻을 수 있는 최대 금액
dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i-j]+prices[j], dp[i])
print(dp[-1])