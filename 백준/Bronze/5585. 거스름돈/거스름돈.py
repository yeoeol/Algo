n = int(input())
rest = 1000-n

arr = [500, 100, 50, 10, 5, 1]

res = 0
for m in arr:
    res += rest//m
    rest %= m
    
print(res)