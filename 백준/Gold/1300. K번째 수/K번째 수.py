n = int(input())
k = int(input())


def check(x):
    cnt = 0
    for i in range(1, n+1):
        cnt += min(x//i, n)
    return cnt


def bin_search():
    ans = 1
    start, end = 1, n*n
    while start <= end:
        mid = (start+end)//2
        cnt = check(mid)
        if cnt >= k:
            ans = mid
            end = mid-1
        else:
            start = mid+1
    return ans
print(bin_search())