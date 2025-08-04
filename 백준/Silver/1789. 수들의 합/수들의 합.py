s = int(input())
ans = 1
for i in range(1, s+1):
    num = i*(i+1) // 2
    if num > s:
        ans = i-1
        break
print(ans)