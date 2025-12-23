dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def check(grid, x, y):
    arr = []    # 가능한 십자가 중심 좌표 및 길이
    length = 1
    while True:
        cnt = 0
        for dx, dy in zip(dxs, dys):
            flag = False
            nx, ny = x+dx*length, y+dy*length
            if not in_range(nx, ny):
                break
            for i in range(min(x, nx), max(x, nx)+1):
                if grid[i][y] != '*':
                    flag = True
                    break
            if flag:
                break
            for j in range(min(y, ny), max(y, ny)+1):
                if grid[x][j] != '*':
                    flag = True
                    break
            if flag:
                break
            cnt += 1

        if cnt == 4:
            arr.append([x, y, length])
            length += 1
        else:
            break
    return arr


def visit(visited, x, y, l):
    visited[x][y] = True
    for i in range(x-l, x+l+1):
        visited[i][y] = True
    for j in range(y-l, y+l+1):
        visited[x][j] = True

def solution(grid, n, m):
    visited = [[False]*m for _ in range(n)]
    arr = []
    for i in range(1, n-1):
        for j in range(1, m-1):
            if grid[i][j] == '*':
                temp = check(grid, i, j)
                if temp:
                    arr.extend(temp)
    for x, y, l in arr:
        visit(visited, x, y, l)

    for i in range(n):
        for j in range(m):
            if grid[i][j] == '*' and not visited[i][j]:
                print(-1)
                return
    print(len(arr))
    for x, y, l in arr:
        print(x+1, y+1, l)

n, m = map(int, input().split())
grid = [list(input()) for _ in range(n)]
solution(grid, n, m)