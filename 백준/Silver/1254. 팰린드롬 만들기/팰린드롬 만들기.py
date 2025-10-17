s = input()

idx = 0


def is_pal(s):
    return s == s[::-1]


for i in range(len(s)):
    if is_pal(s[i:]):
        break
    else:
        idx += 1

print(len(s)+idx)