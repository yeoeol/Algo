import itertools, sys

def input():
    return sys.stdin.readline().strip()

n = int(input())
orders = [2, 3, 4, 5, 6, 7, 8, 9]
inning = [[0] + list(map(int, input().split())) for _ in range(n)]

def calc(order, inning):
    idx = 0
    sco = 0
    # order 순서로 이닝 진행
    for inn in inning:
        base = [0, 0, 0]
        out = 0
        while out < 3:
            cur = order[idx] # 현재 타자
            res = inn[cur]  # 결과
            if res == 0: # 아웃
                out += 1
            elif res == 1: # 안타(1루타)
                sco += base[0]
                base[0], base[1], base[2] = base[1], base[2], 1
            elif res == 2: # 2루타
                sco += (base[0]+base[1])
                base[0], base[1], base[2] = base[2], 1, 0
            elif res == 3:
                sco += (base[0]+base[1]+base[2])
                base[0], base[1], base[2] = 1, 0, 0
            else:
                sco += (base[0]+base[1]+base[2])
                sco += 1 # 홈런 친 타자
                base[0], base[1], base[2] = 0, 0, 0
            idx = (idx+1)%9
    return sco


score = 0
for order in itertools.permutations(orders):
    order = list(order)
    order.insert(3, 1)

    score = max(score, calc(order, inning))
print(score)