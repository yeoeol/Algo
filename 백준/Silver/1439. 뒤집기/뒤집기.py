s = input()
prev = s[0]
cnt0 = 0
cnt1 = 0

if prev == '0': cnt0 += 1
else: cnt1 += 1

for i in range(1, len(s)):
    if prev != s[i]:
        if s[i] == '0':
            cnt0 += 1
        else:
            cnt1 += 1
        prev = s[i]
        
print(min(cnt0, cnt1))