def solution(n, s):
    if s < n:
        return [-1]

    base = s // n
    remainder = s % n

    lst = [base]*n

    for i in range(remainder):
        lst[-(i+1)] += 1

    return lst