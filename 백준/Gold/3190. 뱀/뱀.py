n = int(input())
k = int(input())

board = [[0]*n for _ in range(n)]
board[0][0] = 1
for _ in range(k):
    row, col = map(int, input().split())
    board[row-1][col-1] = 2

l = int(input())
dir_info = {}
for _ in range(l):
    a, b = input().split()
    dir_info[int(a)+1] = b
from collections import deque
snake = deque([(0, 0)])
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우
d = 3 # 처음엔 오른쪽을 향함
x, y = 0, 0 # 뱀의 처음 위치
time = 0
# 1은 뱀, 2는 사과
while True:
    time += 1
    if time in dir_info:
        if dir_info[time] == 'D':
            if d == 0:
                d = 3
            elif d == 1:
                d = 2
            elif d == 2:
                d = 0
            else:
                d = 1
        else:
            if d == 0:
                d = 2
            elif d == 1:
                d = 3
            elif d == 2:
                d = 1
            else:
                d = 0
    nx = x+direction[d][0]
    ny = y+direction[d][1]
    if 0 <= nx < n and 0 <= ny < n:
        if board[nx][ny] == 2: # 사과가 있다면
            snake.append((nx, ny))
            board[nx][ny] = 1
        elif board[nx][ny] == 0:
            tail_x, tail_y = snake.popleft()
            board[tail_x][tail_y] = 0
            board[nx][ny] = 1
            snake.append((nx, ny))
        else:
            print(time)
            break
        x, y = nx, ny
    else:
        print(time)
        break
