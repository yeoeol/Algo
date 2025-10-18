dxs = [0, 0, -1, 0, 1]
dys = [0, 1, 0, -1, 0]

n = int(input())
s = "".join(map(str, input().split()))
m = int(input())
arr = ["".join(map(str, input().split())) for _ in range(m)]
sample = s+s

reversed_s = ""
for i in s[::-1]:
    if i == '1':
        reversed_s += '3'
    elif i == '2':
        reversed_s += '4'
    elif i == '3':
        reversed_s += '1'
    else:
        reversed_s += '2'
sample2 = reversed_s+reversed_s

res = []
for k in range(m):
    if arr[k] in sample or arr[k] in sample2:
        res.append(k)

print(len(res))
for i in res:
    print(*arr[i])
