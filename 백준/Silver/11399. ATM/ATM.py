n = int(input())
p = list(map(int, input().split()))

p.sort()
s = 0
for i in range(n):
    for j in range(i+1):
        s += p[j]

print(s)
