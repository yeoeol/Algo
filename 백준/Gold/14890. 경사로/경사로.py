# 각 행 또는 열이 연속 증가 또는 감소 수열이면서,
# 각 원소의 개수가 L개 연속해야 함
n, L = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def can_go(line):
    N = len(line)
    used = [False] * N  # 경사로 사용 여부 체크

    for i in range(N - 1):
        if line[i] == line[i+1]:
            continue
        elif line[i] + 1 == line[i+1]:  # 오르막
            for j in range(i, i - L, -1):
                if j < 0 or line[j] != line[i] or used[j]:
                    return False
                used[j] = True
        elif line[i] - 1 == line[i+1]:  # 내리막
            for j in range(i + 1, i + L + 1):
                if j >= N or line[j] != line[i+1] or used[j]:
                    return False
                used[j] = True
        else:
            return False
    return True

cnt = 0

for row in grid:
    if can_go(row):
        cnt += 1

for col in zip(*grid):
    if can_go(col):
        cnt += 1

print(cnt)