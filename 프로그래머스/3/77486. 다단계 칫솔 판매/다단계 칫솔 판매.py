def solution(enroll, referral, seller, amount):
    parent = dict()
    for i in range(len(enroll)):
        if referral[i] == '-':
            parent[enroll[i]] = None
        else:
            parent[enroll[i]] = referral[i]

    def dfs(start, money):
        if start is None:
            return
        ten = money*10//100
        result[start] += money-ten
        if ten >= 1:
            dfs(parent[start], ten)

    result = {enroll[i]:0 for i in range(len(enroll))}
    for i, name in enumerate(seller):
        dfs(name, amount[i]*100)

    return [result[e] for e in enroll]