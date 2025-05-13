import sys

def input(): return sys.stdin.readline().strip()


t = int(input())
for _ in range(t):
    l, n = map(int, input().split())

    min_time = -sys.maxsize
    max_time = -sys.maxsize
    for _ in range(n):
        num = int(input())
        if num < l-num:
            min_time = max(min_time, num)
            max_time = max(max_time, l-num)
        else:
            min_time = max(min_time, l-num)
            max_time = max(max_time, num)

    print(min_time, max_time)
