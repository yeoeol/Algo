import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
def input():
    return sys.stdin.readline().strip()


n = int(input())
arr = [0]+list(map(int, input().split()))

cnt = defaultdict(int)

ans = 0
j = 0
for i in range(1, n+1):
    while j+1 <= n and len(cnt) <= 2:
        cnt[arr[j+1]] += 1
        if len(cnt) >= 3:
            del cnt[arr[j+1]]
            break
        j += 1

    ans = max(ans, j-i+1)

    cnt[arr[i]] -= 1
    if cnt[arr[i]] == 0:
        del cnt[arr[i]]

print(ans)