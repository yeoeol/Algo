from collections import defaultdict

n = int(input())

dic = defaultdict(int)
for _ in range(n):
    ext = input().split(".")[1]
    dic[ext] += 1

for ext in sorted(dic):
    print(ext, dic[ext])
