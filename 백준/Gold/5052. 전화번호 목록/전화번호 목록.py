import sys


def input():
    return sys.stdin.readline().strip()

t = int(input())
for _ in range(t):
    n = int(input())
    phones = sorted([input() for _ in range(n)])
    for i in range(n-1):
        if phones[i+1].startswith(phones[i]):
            print("NO")
            break
    else:
        print("YES")

