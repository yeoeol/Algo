n = int(input())

l = [['*' for _ in range(n)] for _ in range(n)]
def rec(k):
    if k == 1:
        return ['*']

    res = []
    star = rec(k//3)
    for S in star:
        res.append(S*3)
    for S in star:
        res.append(S+' '*(k//3)+S)
    for S in star:
        res.append(S*3)

    return res

result = rec(n)
for i in result:
    print(i)