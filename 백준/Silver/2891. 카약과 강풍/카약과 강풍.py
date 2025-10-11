n, s, r = map(int, input().split())
damaged = list(map(int, input().split()))
reserve = list(map(int, input().split()))

for i in reserve[:]:
    if i in damaged:
        reserve.remove(i)
        damaged.remove(i)

damaged.sort()

for d in damaged[:]:
    if d-1 in reserve:
        reserve.remove(d-1)
        damaged.remove(d)
    elif d+1 in reserve:
        reserve.remove(d+1)
        damaged.remove(d)

print(len(damaged))