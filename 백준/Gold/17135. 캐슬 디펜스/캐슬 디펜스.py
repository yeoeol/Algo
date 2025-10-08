import copy, sys
from itertools import combinations

def input():
    return sys.stdin.readline().strip()

n, m, d = map(int, input().split())
original_grid = [list(map(int, input().split())) for _ in range(n)]
archers_positions = list(combinations(range(m), 3))
max_kill_count = 0

def calc_dist(r1, c1, r2, c2):
    return abs(r1-r2)+abs(c1-c2)


for archers in archers_positions:
    grid = copy.deepcopy(original_grid)
    current_kill_count = 0

    for turn in range(n):
        target_to_remove = set()

        for archer_col in archers:
            archer_row = n

            candidates = []
            for r in range(n):
                for c in range(m):
                    if grid[r][c] == 1:
                        dist = calc_dist(archer_row, archer_col, r, c)
                        if dist <= d:
                            candidates.append((dist, c, r))
            if candidates:
                candidates.sort()
                _, target_c, target_r = candidates[0]
                target_to_remove.add((target_r, target_c))

        current_kill_count += len(target_to_remove)
        for r, c in target_to_remove:
            grid[r][c] = 0

        grid.pop(n-1)
        grid.insert(0, [0] * m)

    max_kill_count = max(max_kill_count, current_kill_count)

print(max_kill_count)