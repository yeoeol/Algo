decl = input().split()
base = decl[0]

for s in decl[1:]:
    s = s.rstrip(',;')

    var = ""
    modi = ""

    for c in s:
        if c.isalpha():
            var += c
        else:
            modi += c

    res = base
    for c in modi[::-1]:
        if c == '[':
            continue
        elif c == ']':
            res += '[]'
        else:
            res += c

    print(f"{res} {var};")
