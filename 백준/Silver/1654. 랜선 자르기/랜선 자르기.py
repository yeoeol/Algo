import sys

def input():
    return sys.stdin.readline().strip()

k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]


def check(x):
    cnt = 0
    for elem in arr:
        cnt += elem // x
    return cnt

def bin_search():
    ans = 1
    start, end = 1, max(arr)
    while start <= end:
        mid = (start+end)//2
        cnt = check(mid)
        if cnt >= n:
            ans = mid
            start = mid+1
        else:
            end = mid-1

    return ans

print(bin_search())