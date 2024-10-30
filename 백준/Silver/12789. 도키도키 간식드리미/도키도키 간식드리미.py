import sys
input = sys.stdin.readline

n = int(input().strip())
arr = list(map(int, input().strip().split()))
person = 1
stack = []

for i in arr:
    while stack and (stack[-1] == person):
        stack.pop()
        person += 1
    if i == person:
        person += 1
        continue
    stack.append(i)

flag = True
while stack:
    a = stack.pop()
    if a == person:
        person += 1
        continue
    else:
        flag = False
        break
if flag:
    print("Nice")
else:
    print("Sad")