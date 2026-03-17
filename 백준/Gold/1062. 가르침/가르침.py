import sys
sys.setrecursionlimit(10**7)

def input():
    return sys.stdin.readline().strip()

n, k = map(int, input().split())
if k < 5:
    print(0)
    exit()

words = [set(input()) for _ in range(n)]
visited = [False] * 26

for i in ['a', 'n', 't', 'i', 'c']:
    visited[ord(i)-97] = True

def dfs(start, cnt):
    global res

    if cnt == k-5:
        count = 0
        for word in words:
            if word - learned_set:
                continue
            count += 1
        res = max(res, count)
        return

    for i in range(start, 26):
        if not visited[i]:
            visited[i] = True
            learned_set.add(chr(i+97))
            dfs(i+1, cnt+1)
            visited[i] = False
            learned_set.remove(chr(i+97))

learned_set = {'a', 'n', 't', 'i', 'c'}
res = 0
dfs(0, 0)
print(res)