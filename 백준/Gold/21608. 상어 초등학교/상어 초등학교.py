n = int(input())
leng = n*n
grid = [[0]*n for _ in range(n)]
arr = [[] for _ in range(leng+1)]
order = []
for _ in range(leng):
    lst = list(map(int, input().split()))
    order.append(lst[0])
    arr[lst[0]] = lst[1:]

grid[1][1] = order[0]

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


for i in range(1, leng):
    idx = order[i]
    lst = arr[idx]
    candidates = []
    for x in range(n):
        for y in range(n):
            if grid[x][y] == 0:
                like_cnt = 0
                empty_cnt = 0
                for dx, dy in zip(dxs, dys):
                    nx, ny = x+dx, y+dy
                    if in_range(nx, ny):
                        # 좋아하는 학생 수 세기
                        if grid[nx][ny] in lst:
                            like_cnt += 1
                        # 빈 자리 수 세기
                        elif grid[nx][ny] == 0:
                            empty_cnt += 1
                # 후보 리스트에 저장(정렬 편의성을 위해 좌표에 - 달아주기
                candidates.append((like_cnt, empty_cnt, -x, -y))

    candidates.sort(reverse=True)
    x, y = -candidates[0][2], -candidates[0][3]
    grid[x][y] = idx

score = {0:0, 1:1, 2:10, 3:100, 4:1000}
ans = 0
for x in range(n):
    for y in range(n):
        cnt = 0
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if in_range(nx, ny) and grid[nx][ny] in arr[grid[x][y]]:
                cnt += 1
        ans += score[cnt]
print(ans)