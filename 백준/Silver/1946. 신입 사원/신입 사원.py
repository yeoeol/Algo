import sys


def input():
    return sys.stdin.readline().strip()

t = int(input())
for _ in range(t):
    n = int(input())
    lst = sorted(tuple(map(int, input().split())) for _ in range(n))
    res = n
    # 각 사원마다 자신의 서류 심사 정적이 좋은 사람들 중
    # 면접도 자신보다 순위가 높은 사람이 있다면 탈락
    min_b = lst[0][1]
    for i in range(1, n):
        if min_b < lst[i][1]:
            res -= 1
        else:
            min_b = lst[i][1]

    print(res)
