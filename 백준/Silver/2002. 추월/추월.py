import sys


def input():
    return sys.stdin.readline().strip()

n = int(input())
arr1 = [input() for _ in range(n)]
arr2 = [input() for _ in range(n)]

cnt = 0
while arr1:
    p1 = arr1.pop(0)
    while True:
        p2 = arr2.pop(0)
        if p1 == p2:
            break
        cnt += 1
        arr1.remove(p2)

print(cnt)