import heapq

n, m, k = map(int, input().split())
arr = []
for _ in range(n):
    heapq.heappush(arr, -int(input()))

prev = [0]
while arr:
    num = -heapq.heappop(arr)
    today = prev[-1]//2 + num
    prev.append(today)
    if num-m <= k:
        continue
    heapq.heappush(arr, -(num-m))

print(len(prev)-1)
print(*prev[1:], sep='\n')