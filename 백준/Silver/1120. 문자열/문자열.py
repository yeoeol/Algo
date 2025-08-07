import sys

a, b = input().split()

ans = sys.maxsize

for i in range(len(b)-len(a)+1):
    cnt = 0
    string = b[i:i+len(a)]
    for j in range(len(a)):
        if a[j] != string[j]:
            cnt += 1
    ans = min(ans, cnt)

print(ans)