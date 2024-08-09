import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [i for i in range(n+1)]


def union(a, b):
    fa = find(a)
    fb = find(b)
    if fa < fb:
        arr[fb] = fa
    else:
        arr[fa] = fb


def find(c):
    if arr[c] != c:
        arr[c] = find(arr[c])
    return arr[c]


for _ in range(m):
    num, a, b = map(int, input().split())
    if num == 0:
        union(a, b)
    elif num == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
