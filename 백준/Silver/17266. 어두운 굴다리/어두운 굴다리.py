n = int(input())
m = int(input())
arr = list(map(int, input().split()))

# 첫 번째 등불까지의 거리, 마지막 등불부터 끝까지의 거리
ans = max(arr[0], n - arr[-1])

# 두 등불 사이의 거리 절반 고려
for i in range(m-1):
    ans = max(ans, (arr[i+1] - arr[i] + 1) // 2)

print(ans)
