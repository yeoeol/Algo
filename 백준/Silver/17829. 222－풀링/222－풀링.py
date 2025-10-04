n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

def f(x, y, n):
    if n == 1:
        return grid[x][y]

    half = n//2
    arr = [
        f(x, y, half),
        f(x, y+half, half),
        f(x+half, y, half),
        f(x+half, y+half, half)
    ]
    arr.sort(reverse=True)
    return arr[1]

print(f(0, 0, n))
