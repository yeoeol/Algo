s = input()

i = 0
n = len(s)

while i < n:
    if s[i] != 'w':
        print(0)
        exit()

    cnt = 0
    while i < n and s[i] == 'w':
        cnt += 1
        i += 1

    for ch in 'olf':
        c = 0
        while i < n and s[i] == ch:
            c += 1
            i += 1
        if c != cnt:
            print(0)
            exit()

print(1)