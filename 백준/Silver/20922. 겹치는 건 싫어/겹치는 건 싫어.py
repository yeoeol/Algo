n, k = map(int, input().split())
arr = list(map(int, input().split()))

visited = [0] * 100001
i, j = 0, 0
res = 1
while j < n:
    visited[arr[j]] += 1
    while visited[arr[j]] > k:
        visited[arr[i]] -= 1
        i += 1
    res = max(res, j-i+1)
    j += 1

print(res)