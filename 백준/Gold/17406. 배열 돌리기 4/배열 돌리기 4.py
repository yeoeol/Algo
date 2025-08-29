import sys
from collections import deque
from copy import deepcopy
import itertools

def input():
    return sys.stdin.readline().strip()

n, m, k = map(int, input().split())
grid = [[0] * (m + 1)] + [[0] + list(map(int, input().split())) for _ in range(n)]
rotate = [list(map(int, input().split())) for _ in range(k)]

def rot(arr, start_x, start_y, end_x, end_y):
    for l in range(min(end_x-start_x, end_y-start_y)//2):
        temp = deque()
        # 위 가로
        for j in range(start_y+l, end_y-l):
            temp.append(arr[start_x + l][j])
        # 오른쪽 세로
        for i in range(start_x+l, end_x-l):
            temp.append(arr[i][end_y - l])
        # 아래 가로
        for j in range(end_y-l, start_y+l, -1):
            temp.append(arr[end_x - l][j])
        # 왼쪽 세로
        for i in range(end_x-l, start_x+l, -1):
            temp.append(arr[i][start_y + l])
        temp.rotate(1)

        # 위 가로
        for j in range(start_y+l, end_y-l):
            arr[start_x + l][j] = temp.popleft()
        # 오른쪽 세로
        for i in range(start_x+l, end_x-l):
            arr[i][end_y - l] = temp.popleft()
        # 아래 가로
        for j in range(end_y-l, start_y+l, -1):
            arr[end_x - l][j] = temp.popleft()
        # 왼쪽 세로
        for i in range(end_x-l, start_x+l, -1):
            arr[i][start_y + l] = temp.popleft()
    return arr


def find_min_val(arr):
    res = sys.maxsize
    for g in arr[1:]:
        res = min(sum(g), res)
    return res

answer = sys.maxsize
for item in itertools.permutations(rotate, k):
    arr = deepcopy(grid)
    for r, c, s in item:
        rot(arr, r-s, c-s, r+s, c+s)

    min_val = find_min_val(arr)
    answer = min(answer, min_val)

print(answer)

