from collections import defaultdict

n = int(input())
dic = defaultdict(int)
for _ in range(n):
    dic[input()] += 1

max_cnt = max(dic.values())
ans = []
for key in dic:
    if dic[key] == max_cnt:
        ans.append(key)
print(sorted(ans)[0])