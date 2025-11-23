a, b, c= map(int, input().split())
times = [0]*101
arr = []
for _ in range(3):
    x, y = map(int, input().split())
    arr.append((x, y))
arr.sort()

for x, y in arr:
    for i in range(x, y):
        times[i] += 1
        
res = 0
for i in range(arr[0][0], 101):
    if times[i] == 1:
        res += times[i]*a
    elif times[i] == 2:
        res += times[i]*b
    else:
        res += times[i]*c

print(res)
