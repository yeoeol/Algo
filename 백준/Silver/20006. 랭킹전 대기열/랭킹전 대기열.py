import sys


def input():
    return sys.stdin.readline().strip()

p, m = map(int, input().split())

def matching(level):
    lst = []
    if not dic:
        return lst

    for d in dic:
        low, high = dic[d][0]
        if (low <= level <= high) and len(dic[d][1]) < m:
            lst.append(d)
    return lst

dic = dict()
for i in range(p):
    l, n = input().split()
    l = int(l)
    lst = matching(l)
    if not lst:
        dic[i] = [(l-10, l+10), [(l, n)]]
    elif len(lst) == 1:
        dic[lst[0]][1].append((l, n))
    else:
        lst.sort()
        dic[lst[0]][1].append((l, n))

for key in dic:
    dic[key][1].sort(key=lambda x:x[1])
    if len(dic[key][1]) == m:
        print("Started!")
    else:
        print("Waiting!")

    for level, nickname in dic[key][1]:
        print(level, nickname)
