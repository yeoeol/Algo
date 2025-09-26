r, c = map(int, input().split())
grid = [input() for _ in range(r)]
arr = []

def func(lst):
    s = ''
    for alpha in lst:
        if alpha == '#':
            if len(s) > 1:
                arr.append(s)
            s = ''
        else:
            s += alpha
    if s != '' and len(s) > 1:
        arr.append(s)

for g in grid:
    func(g)
for g in zip(*grid):
    func(g)

print(sorted(arr)[0])