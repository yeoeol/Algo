# 봄 : 자신의 나이만큼 양분을 먹고 나이가 1 증가
# 하나의 칸에 여러 개의 나무 -> 나이가 어린 나무부터 양분 먹기
# 양분이 부족하여 자신의 나이만큼 먹을 수 없다면 죽음

# 여름 : 봄에 죽은 나무가 양분으로 변함
# 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가. 소수점 아래는 버리기

# 가을 : 나무가 번식
# 번식하는 나무는 나이가 5의 배수
# 인접한 8개의 칸에 나이가 1인 나무가 생김

# 겨울 : 땅을 돌아다니면서 땅에 양분 추가
# 각 칸에 추가되는 양분의 양은 A[r][c], 입력으로 주어짐

# K년이 지난 후 살아있는 나무의 개수 구하기
from collections import deque
import sys

def input():
    return sys.stdin.readline().strip()

n, m, k = map(int, input().split())
A = [[0]*(n+1)] + [
    [0]+list(map(int, input().split()))
    for _ in range(n)
]
water = [[5] * (n+1) for _ in range(n+1)]   # 양분

trees = [[deque() for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    x, y, z = map(int, input().split())
    trees[x][y].append(z)

dxs = [-1, -1, 0, 1, 1, 1, 0, -1]
dys = [0, 1, 1, 1, 0, -1, -1, -1]

def in_range(x, y):
    return 1 <= x <= n and 1 <= y <= n

def bfs(trees):
    # 봄 + 여름
    dead = deque()
    for i in range(1, n+1):
        for j in range(1, n+1):
            if not trees[i][j]:
                continue
            alive = deque()
            for age in trees[i][j]:
                if water[i][j] >= age: # 남아있는 양분의 양이 나무의 나이보다 크거나 같다면
                    water[i][j] -= age
                    alive.append(age+1)
                else:
                    dead.append((i, j, age))

            trees[i][j] = alive

    # 여름
    for x, y, age in dead:
        water[x][y] += age//2

    # 가을
    for x in range(1, n+1):
        for y in range(1, n+1):
            for age in trees[x][y]:
                if age % 5 == 0:
                    for dx, dy in zip(dxs, dys):
                        nx, ny = x+dx, y+dy
                        if in_range(nx, ny):
                            trees[nx][ny].appendleft(1)

    # 겨울
    for i in range(1, n+1):
        for j in range(1, n+1):
            water[i][j] += A[i][j]

for _ in range(k):
    bfs(trees)

ans = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        ans += len(trees[i][j])

print(ans)