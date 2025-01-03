a, p = map(int, input().split())
D = [a]

target = -1
while True:
    lst = list(str(D[-1]))
    _sum = 0
    for i in lst:
        _sum += int(i)**p
    if _sum in D:
        target = _sum
        break
    D.append(_sum)
idx = D.index(target)
print(len(D[:idx]))