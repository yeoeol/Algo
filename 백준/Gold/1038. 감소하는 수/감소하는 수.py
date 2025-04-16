n = int(input())

ans = [0, 1, 10]
def dfs(num, depth):
    if depth > 10:
        return
    ans.append(num)
    for i in range(num%10):
        dfs(num*10+i, depth+1)

for i in range(2, 10):
    dfs(i, 0)
ans.sort()

if n >= len(ans):
    print(-1)
else:
    print(ans[n])