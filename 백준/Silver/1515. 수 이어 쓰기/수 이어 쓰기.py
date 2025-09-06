from collections import defaultdict

dic = defaultdict(int)
s = list(input())

idx = 0
num = 1
while idx < len(s):
    ss = str(num)
    for ch in ss:
        if idx < len(s) and ch == s[idx]:
            idx += 1
    num += 1

print(num-1)