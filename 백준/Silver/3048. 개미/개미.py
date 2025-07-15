n1, n2 = map(int, input().split())
first = list(reversed(input()))
second = list(input())

def init_dir():
    dic = dict()
    for f in first:
        dic[f] = 1
    for s in second:
        dic[s] = -1
    return dic

dic = init_dir()

t = int(input())

first.extend(second)
time = 0
while time != t:
    time += 1
    stack = []
    for i in range(n1+n2-1):
        if dic[first[i]] == 1 and dic[first[i+1]] == -1:
            stack.append((i, i+1))
    for i, j in stack:
        first[i], first[j] = first[j], first[i]

print(*first, sep='')
