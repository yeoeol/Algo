def find_block(i, j, board, delete):
    block = board[i][j]
    if block != '-' and block == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
        delete.add((i, j))


def delete_block(board, delete):
    for x, y in delete:
        board[x][y] = board[x][y+1] = board[x+1][y] = board[x+1][y+1] = '-'


def drop_block(m, n, board):
    for i in range(n):
        stack = [board[j][i] for j in range(m) if board[j][i] != '-']
        for row in range(m):
            board[row][i] = '-'
        for row in range(m-len(stack), m):
            board[row][i] = stack[row-(m-len(stack))]

def solution(m, n, board):
    answer = 0
    board = [list(b) for b in board]

    for b in board:
        print(b)
    print('--------original blocks--------')
    while True:
        delete = set()
        for i in range(m-1):
            for j in range(n-1):
                find_block(i, j, board, delete)
        if len(delete) == 0:
            break
        delete_block(board, delete)
        drop_block(m, n, board)
        
    for b in board:
        answer += b.count('-')

    return answer


m = 6
n = 6
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
print(solution(m, n, board))


