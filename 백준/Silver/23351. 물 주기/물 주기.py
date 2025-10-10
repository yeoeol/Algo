n, k, a, b = map(int, input().split())
pots = [k for _ in range(n)]

res = 0

while True:
    pots.sort()
    if pots[0] == 0:
        print(res)
        break
    for i in range(a):
        pots[i] += b
    for i in range(len(pots)):
        pots[i] -= 1
    res += 1
