n = int(input())
m = int(input())
s = input()

ans = 0

cnt = 0
for i in range(m):
    if s[i] == 'O':
        if cnt == 0:
            continue
        if i > 0 and s[i-1] == 'I':
            cnt += 1
        else:
            cnt = 0
    else:
        if i > 0 and s[i-1] == 'O':
            cnt += 1
        else:
            cnt = 1

    if cnt == 2*n+1:
        cnt -= 2
        ans += 1

print(ans)