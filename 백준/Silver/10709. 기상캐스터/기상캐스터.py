h, w = map(int, input().split())
ans = []
for _ in range(h):
    arr = list(input())
    cnt = 0

    lst = []
    is_cloud = False
    for item in arr:
        if item == '.' and not is_cloud:
            lst.append(-1)
        elif item == '.' and is_cloud:
            cnt += 1
            lst.append(cnt)
        elif item == 'c':
            is_cloud = True
            lst.append(0)
            cnt = 0
    ans.append(lst)

for a in ans:
    print(*a)
