def mat_mul(a, b):
    mod = 1000000007
    return [
        [(a[0][0]*b[0][0] + a[0][1]*b[1][0]) % mod,
         (a[0][0]*b[0][1] + a[0][1]*b[1][1]) % mod],
        [(a[1][0]*b[0][0] + a[1][1]*b[1][0]) % mod,
         (a[1][0]*b[0][1] + a[1][1]*b[1][1]) % mod]
    ]


def mat_pow_iter(matrix, n):
    result = [[1, 0], [0, 1]]
    while n > 0:
        if n % 2 == 1:
            result = mat_mul(result, matrix)
        matrix = mat_mul(matrix, matrix)
        n //= 2

    return result


n = int(input())
base = [[1, 1], [1, 0]]
result = mat_pow_iter(base, n - 1)
print(result[0][0])  # F(n)
