n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 절단기의 높이를 최소부터 최대까지 진행(높이가 낮을수록 나무의 양이 많아짐)
# 높이 최소: 1, 최대: max(arr)
# 각각의 높이마다 가져갈 수 있는 나무의 양 카운트
# 계산된 카운트 값이 m보다 크거나 같다면 갱신

# 높이를 파라미터로 받아서 arr 의 h보다 큰, 각 원소에 대해 뺄셈 후 총 나무 양에 더해주기
def get_tree_cnt(h):
    cnt = 0
    for item in arr:
        if item > h:
            cnt += item-h
    return cnt

def bin_search():
    ans = 0
    left, right = 1, max(arr)

    while left <= right:
        mid = (left+right)//2
        cnt = get_tree_cnt(mid)
        if cnt >= m:
            ans = max(ans, mid)
            left = mid+1
        else:
            right = mid-1
    return ans

print(bin_search())