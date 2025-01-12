button = [300, 60, 10]
result = [0, 0, 0]

t = int(input())
idx = 0
while True:
    if t < button[idx]:
        idx += 1
        if idx >= 3:
            print(-1)
            exit(0)
        continue
    q = t//button[idx]
    r = t%button[idx]
    t = r
    result[idx] += q
    if t == 0:
        break

print(*result)