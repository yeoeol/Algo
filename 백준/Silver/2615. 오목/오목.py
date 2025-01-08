d = [(1, 0), (0, 1), (-1, 1), (1, 1)]    # ↓, →, ↗, ↘

go = [list(map(int, input().split())) for _ in range(19)]
for i in range(19):
    for j in range(19):
        if go[i][j] != 0:
            cur_color = go[i][j]
            for k in range(len(d)):
                cnt = 1
                dx, dy = d[k]   # 방향
                prev_x, prev_y = i-dx, j-dy
                if 0 <= prev_x < 19 and 0 <= prev_y < 19 and go[prev_x][prev_y] == cur_color:
                    continue
                nx, ny = i+dx, j+dy
                while 0 <= nx < 19 and 0 <= ny < 19 and go[nx][ny] == cur_color:
                    cnt += 1
                    nx, ny = nx+dx, ny+dy

                if cnt == 5:    # 육목인지 확인
                    print(cur_color)
                    print(i+1, j+1)
                    exit(0)
print(0)
