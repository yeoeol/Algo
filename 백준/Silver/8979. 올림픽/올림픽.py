N, K = map(int, input().split())
arr = []
for _ in range(N):
    country, gold, silver, bronze = map(int, input().split())
    arr.append([country, gold, silver, bronze])

arr.sort(key=lambda x:(x[1], x[2], x[3]), reverse=True)

rank = [0]*(N+1)
i = 1
r = 1
rank[1] = 1
prev = arr[0][1:]
while True:
    if i >= N:
        break
    if prev == arr[i][1:]:
        rank[arr[i][0]] = rank[arr[i-1][0]]
        i += 1
        r += 1
        continue
    r += 1
    rank[arr[i][0]] = r
    prev = arr[i][1:]
    i += 1
print(rank[K])