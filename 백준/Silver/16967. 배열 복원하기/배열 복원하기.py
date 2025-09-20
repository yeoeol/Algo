h, w, x, y = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(h+x)]
A = [[0] * w for _ in range(h)]


for i in range(h):
    for j in range(w):
        if i >= x and j >= y:
            A[i][j] = B[i][j] - A[i-x][j-y]
        else:
            A[i][j] = B[i][j]
for a in A:
    print(*a)
