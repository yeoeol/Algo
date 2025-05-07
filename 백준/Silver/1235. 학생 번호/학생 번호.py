import sys

def input():
    return sys.stdin.readline().strip()

n = int(input())
arr = [input() for _ in range(n)]

lst = set()
for i in range(1, len(arr[0])+1):
    for a in arr:
        lst.add(a[-1:-1-i:-1])
    if len(lst) == n:
        print(i)
        break
    lst.clear()
