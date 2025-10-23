n, m = map(int, input().split())
girl_group = dict()
for _ in range(n):
    name = input()
    girl_group[name] = []

    k = int(input())
    for _ in range(k):
        girl_group[name].append(input())

for _ in range(m):
    name = input()
    o = int(input())
    if o == 0:
        girl_group[name].sort()
        print(*girl_group[name], sep='\n')
    else:
        for team in girl_group:
            if name in girl_group[team]:
                print(team)
                break
