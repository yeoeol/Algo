def is_prime(n):
    prime = [True] * (n+1)
    for p in range(2, int(n**0.5) + 1):
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False

    prime_numbers = [p for p in range(2, n + 1) if prime[p]]
    return prime_numbers


n = int(input())
sosu = is_prime(n)
i, j = 0, 0
_sum = 0
res = 0
while True:
    if i == len(sosu):
        break
    if _sum >= n:
        if _sum == n:
            res += 1
        _sum -= sosu[i]
        i += 1
    else:
        _sum += sosu[j]
        j += 1
        if j == len(sosu):
            j -= 1


print(res)