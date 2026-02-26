f = [0]*70
f[0] = 1
f[1] = 1
f[2] = 2
f[3] = 4
for i in range(4, 70):
    f[i] = f[i-1] + f[i-2] + f[i-3] + f[i-4]

t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    ans.append(f[n])
print(*ans, sep='\n')