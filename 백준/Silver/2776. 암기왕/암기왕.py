t = int(input())



def bin_search(x):
    left, right = 0, n-1
    while left <= right:
        mid = (left+right) // 2
        if arr1[mid] == x:
            return True
        if arr1[mid] < x:
            left = mid+1
        else:
            right = mid-1
    return False

for _ in range(t):
    n = int(input())
    arr1 = sorted(map(int, input().split()))
    m = int(input())
    arr2 = list(map(int, input().split()))
    for i in arr2:
        if bin_search(i):
            print(1)
        else:
            print(0)