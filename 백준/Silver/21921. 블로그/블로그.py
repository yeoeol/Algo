n, x = map(int, input().split())
arr = [0]+list(map(int, input().split()))

prefix = [0]*(n+1)
for i in range(1, n+1):
    prefix[i] = prefix[i-1]+arr[i]

ans = 0
for i in range(x, n+1):
    visitor = prefix[i]-prefix[i-x]
    ans = max(ans, visitor)
    
if ans == 0:
    print("SAD")
else:
    cnt = 0
    for i in range(x, n+1):
        visitor = prefix[i]-prefix[i-x]
        if ans == visitor:
            cnt += 1
    print(ans)
    print(cnt)
