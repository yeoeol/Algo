n, m = map(int, input().split())
pac = []
unit = []
for _ in range(m):
    a, b = map(int, input().split())
    pac.append(a)
    unit.append(b)
val6 = min(pac)
val1 = min(unit)

res = 0
if val6 >= val1*6:
    res = val1*n
else:
    if n >= 6:
        res += (n//6)*val6
        n = n%6
    res += min(n*val1, val6)
print(res)
