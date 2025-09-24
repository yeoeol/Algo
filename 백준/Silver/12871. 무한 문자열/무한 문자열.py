s = input()
t = input()
m = max(len(s), len(t))
new_s = s*m
new_t = t*m

if s[0] != t[0]:
    print(0)
elif len(new_s) <= len(new_t) and new_s in new_t:
    print(1)
elif len(new_s) > len(new_t) and new_t in new_s:
    print(1)
else:
    print(0)