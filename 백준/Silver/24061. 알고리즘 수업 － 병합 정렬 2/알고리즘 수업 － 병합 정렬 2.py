def merge(arr, s, m, e):
    global cnt, ans

    i, j = s, m+1
    tmp = []
    while i <= m and j <= e:
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1

    while i <= m:
        tmp.append(arr[i])
        i += 1
    while j <= e:
        tmp.append(arr[j])
        j += 1
    i, t = s, 0
    while i <= e:
        arr[i] = tmp[t]
        i += 1
        t += 1

        cnt += 1
        if cnt == k:
            ans = arr[:]


def merge_sort(arr, s, e):
    if s < e:
        m = (s+e)//2
        merge_sort(arr, s, m)
        merge_sort(arr, m+1, e)
        merge(arr, s, m, e)

n, k = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0
ans = []
merge_sort(A, 0, len(A)-1)
if len(ans) == 0:
    print(-1)
else:
    print(*ans)

