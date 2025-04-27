s = input()
prev = s[0]
ans = 10

for i in range(1, len(s)):
    if s[i] == prev:
        ans += 5
    else:
        ans += 10
    prev = s[i]
print(ans)