from collections import defaultdict

n = int(input())
names = [input() for _ in range(n)]

dic = defaultdict(int)
for name in names:
    dic[name[0]] += 1

ans = []
for key, value in dic.items():
    if value >= 5:
        ans.append(key)
if ans:
    ans.sort()
    print(''.join(ans))
else:
    print("PREDAJA")