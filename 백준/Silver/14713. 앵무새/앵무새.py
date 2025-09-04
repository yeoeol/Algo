from collections import deque

n = int(input())
sentences = [deque(input().split()) for _ in range(n)]
l = input().split()

for word in l:
    found = False
    for s in sentences:
        if s and s[0] == word:
            s.popleft()
            found = True
            break
    if not found:
        print("Impossible")
        exit()

if all(len(s) == 0 for s in sentences):
    print("Possible")
else:
    print("Impossible")
