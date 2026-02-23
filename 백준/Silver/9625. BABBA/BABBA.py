k = int(input())

ans = (0, 1)
for i in range(2, k+1):
    ans = (ans[1], ans[0]+ans[1])
    
print(*ans)