import itertools

def eq(lst1, lst2):
    return len(set(lst1).intersection(set(lst2)))

def solution(n, q, ans):
    m = len(q)
    lst = list(range(1, n+1))
    res = 0
    for g in itertools.combinations(lst, 5):
        for i in range(m):
            if eq(g, q[i]) != ans[i]:
                break
        else:
            res += 1
    return res