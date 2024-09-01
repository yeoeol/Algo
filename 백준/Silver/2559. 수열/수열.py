import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))

l = [sum(arr[:k])]
for i in range(1, n-k+1):
    l.append(l[-1]-arr[i-1]+arr[i+k-1])

print(max(l))
