n, l = map(int, input().split())
dic = dict()
for _ in range(n):
    d, r, g = map(int, input().split())
    dic[d] = (r, g)

t = 0
location = 0
while location < l:
    if location in dic:
        r, g = dic[location]
        flag = t % (r+g)
        if flag < r:
            t += 1
            continue
    location += 1
    t += 1

print(t)