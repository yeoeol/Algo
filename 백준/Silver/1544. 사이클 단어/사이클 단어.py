n = int(input())
groups = []

for _ in range(n):
    word = input()
    is_new = True

    for g in groups:
        if len(word) == len(g) and word in g + g:
            is_new = False
            break

    if is_new:
        groups.append(word)

print(len(groups))