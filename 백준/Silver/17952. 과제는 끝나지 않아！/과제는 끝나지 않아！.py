import sys

def input():
    return sys.stdin.readline().strip()

n = int(input())
ans = 0
prev = [0, 0] # 점수, 시간
stack = []
for _ in range(n):
    lst = list(map(int, input().split()))
    if lst[0] == 1:
        if lst[2] == 1:
            ans += lst[1]
            continue
             
        if not (prev[0] == 0 and prev[1] == 0):
            stack.append([prev[0], prev[1]])
        prev[0] = lst[1]
        prev[1] = lst[2]-1
    else:
        prev[1] -= 1
        if prev[1] == 0:
            ans += prev[0]
            if not stack:
                prev = [0, 0]
            else:
                prev = stack.pop()
print(ans)
