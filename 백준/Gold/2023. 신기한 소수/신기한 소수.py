n = int(input())
arr = [2, 3, 5, 7]

# def era(n):
#     primes = [True] * (n+1)
#     primes[0] = primes[1] = False
#     end = n**0.5
#     for i in range(2, int(end)+1):
#         if primes[i]:
#             for j in range(i*i, n+1, i):
#                 primes[j] = False
#     return primes
#
# primes = era(10 ** n)
# lst = []

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True


def rec(num, cnt):
    if cnt == n:
        print(num)
        return

    for i in [1,3,7,9]:
        next_num = num * 10 + i
        if is_prime(next_num):
            rec(next_num, cnt+1)

for start in arr:
    rec(start, 1)
