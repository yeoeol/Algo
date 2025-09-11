n = int(input())
grid = [list(input()) for _ in range(n)]
flag = False
for i in range(n):
    for j in range(n):
        if grid[i][j] == '*':
            x, y = i+1, j
            flag = True
            break
    if flag:
        break

print(x+1, y+1)

res = [0, 0, 0, 0, 0]
for j in range(y-1, -1, -1):
    if grid[x][j] == '_':
        break
    res[0] += 1
for j in range(y+1, n):
    if grid[x][j] == '_':
        break
    res[1] += 1

end = -1
for i in range(x+1, n):
    if grid[i][y] == '_':
        end = i
        break
    res[2] += 1

for i in range(end, n):
    if grid[i][y-1] == '*':
        res[3] += 1
    if grid[i][y+1] == '*':
        res[4] += 1

print(*res)