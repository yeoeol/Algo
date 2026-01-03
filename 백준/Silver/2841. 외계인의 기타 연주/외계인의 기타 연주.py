import sys

def input():
    return sys.stdin.readline().strip()

n, p = map(int, input().split())
arr = [[] for _ in range(7)]
ans = 0
for _ in range(n):
    num, p = map(int, input().split())

    while arr[num] and arr[num][-1] > p:
        arr[num].pop()
        ans += 1
    if arr[num] and arr[num][-1] == p:
        continue
    arr[num].append(p)
    ans += 1

print(ans)
