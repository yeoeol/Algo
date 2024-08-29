import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
l = [0]
cur = 0
for i in range(n):
    cur += arr[i]
    l.append(cur)

for _ in range(m):
    a, b = map(int, input().rstrip().split())
    print(l[b]-l[a-1])