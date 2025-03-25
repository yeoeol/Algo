n, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()
# 한 집에는 공유기 하나만 설치 가능
# 가장 인접한 공유기 사이의 거리를 가능한 크게 하여 설치
# C개의 공유기를 N개의 집에 적당히 설치, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램

# 최소 거리, 최대 거리 d
# 최소 거리와 최대 거리 사이 값을 넣어서 최적값 찾기
def check(dist):
    cnt = 1
    prev = arr[0]
    for i in range(1, len(arr)):
        if arr[i]-prev >= dist:
            cnt += 1
            prev = arr[i]

    return cnt

def bin_search(c, min_d, max_d):
    max_dist = 0
    left, right = min_d, max_d
    while left <= right:
        mid = (left+right)//2
        cnt = check(mid)
        if cnt >= c:
            max_dist = mid
            left = mid+1
        else:
            right = mid-1
    return max_dist

print(bin_search(c, 1, arr[-1]-arr[0]))