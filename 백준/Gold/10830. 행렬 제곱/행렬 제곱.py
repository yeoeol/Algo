n, b = map(int, input().split())
grid = [tuple(map(int, input().split())) for _ in range(n)]
mod = 1000
def mat_mul(A, B):
    size = n
    result = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] += A[i][k] * B[k][j]
            result[i][j] %= mod  # 매 연산 후 나머지
    return result

def rec(matrix, b):
    if b == 1:
        return [[e % mod for e in row] for row in grid]

    temp = rec(matrix, b // 2)
    temp = mat_mul(temp, temp)
    if b % 2 == 0:
        return temp
    else:
        return mat_mul(temp, matrix)

for r in rec(grid, b):
    print(*r)
