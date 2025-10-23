from collections import Counter

n, c = map(int, input().split())
arr = list(map(int, input().split()))

orders = dict()
for i, key in enumerate(arr):
    if key in orders:
        continue
    orders[key] = i

count = sorted(Counter(arr).items(), key=lambda x:(x[1], -orders[x[0]]), reverse=True)

for i in range(len(count)):
    for _ in range(count[i][1]):
        print(count[i][0], end=' ')
