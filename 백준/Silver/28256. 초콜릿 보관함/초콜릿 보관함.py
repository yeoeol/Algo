dxs = [-1, 1, 0, 0]
dys = [0, 0, 1, -1]

def in_range(x, y):
    return 0 <= x < 3 and 0 <= y < 3


def dfs(x, y):
    global lst
    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if in_range(nx, ny) and visited[nx][ny] == -1 and grid[nx][ny] == 'O':
            lst.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1
            dfs(nx, ny)


t = int(input())
for _ in range(t):
    grid = [input() for _ in range(3)]
    arr = list(map(int, input().split()))
    n = arr[0]
    arr = arr[1:]
    
    visited = [[-1]*3 for _ in range(3)]
    ans = []
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 'O' and visited[i][j] == -1:
                lst = [(i, j)]
                visited[i][j] = 0
                dfs(i, j)
                ans.append(len(lst))
    ans.sort()
    
    print(1 if arr == ans else 0)
