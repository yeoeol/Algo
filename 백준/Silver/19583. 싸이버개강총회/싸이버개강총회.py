import sys

s, e, q = input().split()

before = set()
after = set()
for line in sys.stdin:
    time, name = line.strip().split()
    if time <= s:
        before.add(name)
    elif e <= time <= q:
        if name in before:
            after.add(name)

print(len(after))
