c = input().split('-')
t = []

for i in c:
    s = 0
    tmp = i.split('+')
    for j in tmp:
        s += int(j)
    t.append(s)

s = t[0]
for i in range(1, len(t)):
    s -= t[i]

print(s)