import itertools

x = input()

def solution(n):
    lst = list(itertools.permutations(n, len(n)))
    arr = []
    for l in lst:
        arr.append(int("".join(l)))
    arr.sort()
    for num in arr:
        if num > int(x):
            return num
    return 0

print(solution(list(x)))
