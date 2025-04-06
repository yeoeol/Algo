from collections import defaultdict
import sys

input = sys.stdin.readline

tm = defaultdict(int)

c = 0
while True:
    word = input().strip()
    if not word:
        break
    tm[word] = tm[word]+1
    c += 1

for w, cnt in sorted(tm.items()):
    print(f"{w} {cnt*100/c:.4f}")
