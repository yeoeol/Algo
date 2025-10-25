n = int(input())
grid = [list(input()) for _ in range(n)]

res = -1
for i in range(n):
    friend = set()
    for j in range(n):
        if i == j:
            continue
        if grid[i][j] == 'Y':
            friend.add(j)
        else:
            for k in range(n):
                if grid[i][k] == 'Y' and grid[k][j] == 'Y':
                    friend.add(j)
                    break
    res = max(res, len(friend))
print(res)