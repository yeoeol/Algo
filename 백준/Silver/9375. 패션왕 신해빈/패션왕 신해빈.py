from collections import defaultdict

t = int(input())
for _ in range(t):
    dic = defaultdict(int)

    n = int(input())
    for _ in range(n):
        name, sort = input().split()
        dic[sort] += 1

    types = list(dic.values())
    ans = 1
    for cnt in types:
        ans *= (cnt+1)
    print(ans-1)