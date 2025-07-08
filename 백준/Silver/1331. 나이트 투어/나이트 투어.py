dic = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5}
dxs = [1, 2, 2, 1, -1, -2, -2, -1]
dys = [2, 1, -1, -2, -2, -1, 1, 2]

s = input()
x, y = dic[s[0]], int(s[1])-1
start_x, start_y = dic[s[0]], int(s[1])-1
visited = [[False]*6 for _ in range(6)]
visited[start_x][start_y] = True

flag = True
for _ in range(35):
    s = input()
    target_x, target_y = dic[s[0]], int(s[1])-1
    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if target_x == nx and target_y == ny and not visited[nx][ny]:
            x, y = nx, ny
            visited[x][y] = True
            break
    else:
        flag = False
        break

if not flag:
    print("Invalid")
elif all(visited[i][j] for i in range(6) for j in range(6)):
    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if start_x == nx and start_y == ny:
            print("Valid")
            break
    else:
        print("Invalid")
else:
    print("Invalid")