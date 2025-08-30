import sys

def input():
    return sys.stdin.readline().strip()

n, m, k = map(int, input().split())
fireballs = []
for _ in range(m):
    r, c, mm, s, d = map(int, input().split())
    fireballs.append((r-1, c-1, mm, s, d))

dxs = [-1, -1, 0, 1, 1, 1, 0, -1]
dys = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(k):
    # [질량 합, 속력 합, 방향 리스트, 개수]
    grid = [[[0, 0, [], 0] for _ in range(n)] for _ in range(n)]

    # 모든 파이어볼 이동
    while fireballs:
        r, c, mm, s, d = fireballs.pop()
        dx, dy = dxs[d], dys[d]
        r, c = (r+s*dx) % n, (c+s*dy) % n
        grid[r][c][0] += mm
        grid[r][c][1] += s
        grid[r][c][2].append(d)  # 방향을 리스트로 저장
        grid[r][c][3] += 1

    # 합쳐진 파이어볼 처리
    for i in range(n):
        for j in range(n):
            mass_sum, speed_sum, dirs, cnt = grid[i][j]
            if cnt == 0:
                continue
            if cnt == 1:  # 그대로 다시 추가
                fireballs.append((i, j, mass_sum, speed_sum, dirs[0]))
            else:  # 2개 이상 합쳐진 경우
                new_mass = mass_sum // 5
                if new_mass == 0:
                    continue
                new_speed = speed_sum // cnt

                all_even = all(d % 2 == 0 for d in dirs)
                all_odd = all(d % 2 == 1 for d in dirs)

                if all_even or all_odd:
                    new_dirs = [0, 2, 4, 6]
                else:
                    new_dirs = [1, 3, 5, 7]

                for nd in new_dirs:
                    fireballs.append((i, j, new_mass, new_speed, nd))

# 최종 질량 합 출력
print(sum(f[2] for f in fireballs))
