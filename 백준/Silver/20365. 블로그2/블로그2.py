n = int(input())
s = input()

b_cnt = 0
r_cnt = 0

for i in range(1, len(s)):
    if s[i] != s[i-1]:
        if s[i-1] == 'B':
            b_cnt += 1
        elif s[i-1] == 'R':
            r_cnt += 1
if s[len(s)-1] == 'R':
    r_cnt += 1
else:
    b_cnt += 1
print(min(r_cnt, b_cnt)+1)