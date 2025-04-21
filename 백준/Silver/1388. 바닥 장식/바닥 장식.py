n, m = map(int, input().split())
grid = [list(input()) for _ in range(n)]

ans = 0
for g in grid:
    flag = False
    for i in range(len(g)):
        if g[i] == '-' and not flag:
            flag = True
            ans += 1
        elif g[i] == '|':
            flag = False

for g in zip(*grid):
    flag = False
    for i in range(len(g)):
        if g[i] == '|' and not flag:
            flag = True
            ans += 1
        elif g[i] == '-':
            flag = False

print(ans)