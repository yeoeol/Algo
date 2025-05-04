n = int(input())
A = sorted(list(map(int, input().split())))
m = int(input())
B = list(map(int, input().split()))


def bin_search(A, target):
    left, right = 0, len(A)-1
    while left <= right:
        mid = (left+right)//2
        if A[mid] == target:
            return True
        if target < A[mid]:
            right = mid-1
        else:
            left = mid+1
    return False

for b in B:
    if bin_search(A, b): # A 배열 안에 b가 존재하는지
        print(1)
    else:
        print(0)
