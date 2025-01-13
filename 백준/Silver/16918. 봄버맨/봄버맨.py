dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

r, c, n = map(int, input().split())
board = [list(input()) for _ in range(r)]
bomb = []


def find_bomb():
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'O':
                bomb.append((i, j))

def bust_bomb():
    while bomb:
        px, py = bomb.pop()
        board[px][py] = '.'
        for d in range(4):
            nx, ny = px+dx[d], py+dy[d]
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            board[nx][ny] = '.'

def put_bomb():
    global board
    board = [['O']*c for _ in range(r)]


for t in range(1, n+1):
    if t == 1:
        find_bomb()
    elif t % 2 == 1:
        bust_bomb()
        find_bomb()
    else:
        put_bomb()

for i in board:
    print(''.join(i))
