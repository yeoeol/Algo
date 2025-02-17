def east(lst):
    temp = [lst[3], lst[1], lst[0], lst[5], lst[4], lst[2]]
    return temp

def west(lst):
    temp = [lst[2], lst[1], lst[5], lst[0], lst[4], lst[3]]
    return temp

def north(lst):
    temp = [lst[4], lst[0], lst[2], lst[3], lst[5], lst[1]]
    return temp

def south(lst):
    temp = [lst[1], lst[5], lst[2], lst[3], lst[0], lst[4]]
    return temp

def direc(d, lst):
    if d == 1:
        lst = east(lst)
    elif d == 2:
        lst = west(lst)
    elif d == 3:
        lst = north(lst)
    else:
        lst = south(lst)
    return lst

n, m, x, y, k = map(int, input().split())
# 동(1), 서(2), 북(3), 남(4)

board = [list(map(int, input().split())) for _ in range(n)]
# 동쪽으로 굴림 -> [1,2,3,4,5,6] [4,2,1,6,5,3]
# 서쪽으로 굴림 -> [1,2,3,4,5,6] [3,2,6,1,5,4]
# 북쪽으로 굴림 -> [1,2,3,4,5,6] [5,1,3,4,6,2]
# 남쪽으로 굴림 -> [1,2,3,4,5,6] [2,6,3,4,1,5]

mv = [(0, 1), (0, -1), (-1, 0), (1, 0)] # 동서북남
dice = [0, 0, 0, 0, 0, 0]
orders = list(map(int, input().split()))
for order in orders:
    dx, dy = mv[order-1]
    nx, ny = x+dx, y+dy
    if 0 <= nx < n and 0 <= ny < m:
        # 주사위 굴리기
        dice = direc(order, dice)
        x, y = nx, ny
        # 지도 확인
        if board[x][y] == 0: # 이동한 칸에 쓰여 있는 수가 0이면
            board[x][y] = dice[-1]
        else:
            dice[-1] = board[x][y]
            board[x][y] = 0
        print(dice[0])
