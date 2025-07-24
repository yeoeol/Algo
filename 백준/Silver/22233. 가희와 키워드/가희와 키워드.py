import sys
from collections import defaultdict

def input():
    return sys.stdin.readline().strip()

n, m = map(int, input().split())

keyword = defaultdict(int)
for _ in range(n):
    keyword[input()] += 1

for _ in range(m):
    keywords = input().split(",")
    for key in keywords:
        keyword[key] -= 1
        if keyword[key] <= 0:
            keyword.pop(key)
    print(len(keyword))