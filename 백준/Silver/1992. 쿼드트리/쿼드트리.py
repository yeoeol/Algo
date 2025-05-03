# 흰 점 0, 검은 점 1
n = int(input())
grid = [list(input()) for _ in range(n)]

def rec(x, y, size):
    num = grid[x][y]
    if all(grid[i][j] == num for i in range(x, x + size) for j in range(y, y + size)):
        return str(num)
    else:
        half = size // 2
        return "(" + \
            rec(x, y, half) + \
            rec(x, y + half, half) + \
            rec(x + half, y, half) + \
            rec(x + half, y + half, half) + ")"

ans = rec(0, 0, n)
print(ans)