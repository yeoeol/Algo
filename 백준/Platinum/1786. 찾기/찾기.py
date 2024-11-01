def make_table(P):
    lp = len(P)
    table = [0]*lp
    i = 0
    for j in range(1, lp):
        while i > 0 and P[i] != P[j]:
            i = table[i-1]

        if P[i] == P[j]:
            i += 1
            table[j] = i

    return table

def KMP(word, pattern):
    table = make_table(pattern)

    res = []
    i = 0
    for j in range(len(word)):
        while i > 0 and word[j] != pattern[i]:
            i = table[i-1]

        if word[j] == pattern[i]:
            if i == len(pattern)-1:
                res.append(j-len(pattern)+2)
                i = table[i]
            else:
                i += 1

    return res


s1 = input()
s2 = input()
r = KMP(s1, s2)
print(len(r))
print(*r)