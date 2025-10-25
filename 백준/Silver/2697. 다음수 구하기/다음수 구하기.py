import sys

def input():
    return sys.stdin.readline().strip()

t = int(input())

def find_criteria(s):
    ind = len(s)-1
    for i in range(len(s)-1, 0, -1):
        if s[i-1] < s[i]:
            ind = i-1
            break
    return ind


for _ in range(t):
    inp = input()
    a = list(map(int, list(inp)))
    idx = find_criteria(a)
    for i in range(len(a)-1, idx, -1):
        if a[idx] < a[i]:
            a[i], a[idx] = a[idx], a[i]
            break

    res = "".join(map(str, a[:idx+1] + sorted(a[idx+1:])))
    if res == inp:
        print("BIGGEST")
    else:
        print(res)
