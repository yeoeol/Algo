n, k = map(int, input().split())
coins = []

for i in range(n):
    coins.append(int(input()))

s = 0
i = len(coins)-1
while True:
    if coins[i] > k:
        i -= 1
        continue
    s += k//coins[i]
    k %= coins[i]
    if k == 0:
        break

print(s)