import sys
from collections import deque

def input():
    return sys.stdin.readline().strip()

n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

for layer in range(min(n, m) // 2):
    temp = deque()

    # 왼쪽 세로
    for i in range(layer, n-layer):
        temp.append(arr[i][layer])
    # 아래 가로
    for j in range(layer+1, m-layer):
        temp.append(arr[n-layer-1][j])
    # 오른쪽 세로
    for i in range(n-layer-2, layer-1, -1):
        temp.append(arr[i][m-layer-1])
    # 위 가로
    for j in range(m-layer-2, layer, -1):
        temp.append(arr[layer][j])

    temp.rotate(r)

    idx = 0
    # 왼쪽 세로
    for i in range(layer, n-layer):
        arr[i][layer] = temp[idx]
        idx += 1
    # 아래 가로
    for j in range(layer+1, m-layer):
        arr[n-layer-1][j] = temp[idx]
        idx += 1
    # 오른쪽 세로
    for i in range(n-layer-2, layer-1, -1):
        arr[i][m-layer-1] = temp[idx]
        idx += 1
    # 위 가로
    for j in range(m-layer-2, layer, -1):
        arr[layer][j] = temp[idx]
        idx += 1

for a in arr:
    print(*a)