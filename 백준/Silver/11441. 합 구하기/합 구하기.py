import sys
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
arr = [0]+list(map(int, input().split()))

prefix = [0]*(n+1)
for i in range(1, n+1):
    prefix[i] = prefix[i-1]+arr[i]

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(prefix[b]-prefix[a-1])