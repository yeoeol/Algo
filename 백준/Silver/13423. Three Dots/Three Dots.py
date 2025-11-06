import sys


def input():
    return sys.stdin.readline().strip()

t = int(input())


def solution(n, arr):
    sets = set(arr)
    cnt = 0
    for a in range(n-2):
        for b in range(a+1, n-1):
            ba = arr[b]-arr[a]
            if (arr[b]+ba) in sets:
                cnt += 1
    return cnt

for _ in range(t):
    n = int(input())
    arr = sorted(map(int, input().split()))
    print(solution(n, arr))