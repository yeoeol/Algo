t = int(input())
for _ in range(t):
    cry = input().split()
    sets = set()
    while True:
        s = input()
        if s == 'what does the fox say?':
            break
        sets.add(s.split()[2])

    res = []
    for word in cry:
        if word not in sets:
            res.append(word)
    print(*res)