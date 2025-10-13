r, c = map(int, input().split())
grid = [input() for _ in range(r)]
arr = []
for i in range(r):
    s = ""
    for j in range(c):
        if grid[i][j] == '#':
            if len(s) >= 2:
                arr.append(s)
            s = ""
            continue
        s += grid[i][j]
    if len(s) >= 2:
        arr.append(s)

for j in range(c):
    s = ""
    for i in range(r):
        if grid[i][j] == '#':
            if len(s) >= 2:
                arr.append(s)
            s = ""
            continue
        s += grid[i][j]
    if len(s) >= 2:
        arr.append(s)
        
arr.sort()
print(arr[0])