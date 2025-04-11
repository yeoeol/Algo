import sys

def input():
    return sys.stdin.readline().strip()

n = int(input())
p = int(input())

parent = [i for i in range(n+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x, y = find(x), find(y)
    parent[x] = y

ans = 0
for i in range(1, p+1):
    num = int(input())
    # i가 1~num 번째 게이트 중 하나에 영구적으로 도킹
    # 다 차있다면 공항 폐쇄
    find_gate = find(num)
    if find_gate == 0:
        break

    union(find_gate, find_gate-1)
    ans += 1

print(ans)