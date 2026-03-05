n = int(input())
L = list(map(int, input().split()))
J = list(map(int, input().split()))
arr = list(zip(L, J))

dp = [0] * 100 # 체력 i를 사용했을 때 얻을 수 있는 최대 기쁨

for hp, happy in arr:
    for h in range(99, hp-1, -1):
        dp[h] = max(dp[h], dp[h-hp]+happy)
print(dp[-1])