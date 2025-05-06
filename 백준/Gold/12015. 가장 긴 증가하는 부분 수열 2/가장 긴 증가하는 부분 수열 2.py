n = int(input())
arr = list(map(int, input().split()))
dp = []


def bin_search(x):
    left, right = 0, len(dp)-1
    while left <= right:
        mid = (left+right)//2
        if x <= dp[mid]:
            right = mid-1
        else:
            left = mid+1
    return left

for elem in arr:
    if not dp or dp[-1] < elem:
        dp.append(elem)
    else:
        idx = bin_search(elem)
        dp[idx] = elem

print(len(dp))