from collections import deque

# 1: 오른쪽, 2: 아래, 3: 왼쪽, 4: 위
dr = [0, 0, 1, 0, -1]
dc = [0, 1, 0, -1, 0]


def solution(board, commands):
    n = len(board)
    m = len(board[0])

    def get_group(start, direction):
        group = set([start])
        q = deque([start])

        while q:
            cur = q.popleft()

            for r in range(n):
                for c in range(m):
                    if board[r][c] != cur:
                        continue

                    nr = (r + dr[direction]) % n
                    nc = (c + dc[direction]) % m

                    nxt = board[nr][nc]

                    if nxt != 0 and nxt not in group:
                        group.add(nxt)
                        q.append(nxt)

        return group

    def move_group(group, direction):
        cells = []

        for r in range(n):
            for c in range(m):
                if board[r][c] in group:
                    cells.append((r, c, board[r][c]))

        # 기존 위치 전부 비우기
        for r, c, app in cells:
            board[r][c] = 0

        # 새 위치에 동시에 배치
        for r, c, app in cells:
            nr = (r + dr[direction]) % n
            nc = (c + dc[direction]) % m
            board[nr][nc] = app

    def find_broken_apps(direction):
        broken = []
        added = set()

        # 좌우 이동
        if direction in (1, 3):
            for r in range(n):
                left = board[r][0]
                right = board[r][m - 1]

                if left == 0 or left != right:
                    continue

                # 행 전체가 같은 앱으로 꽉 차 있으면 잘린 것이 아님
                all_same = True
                for c in range(m):
                    if board[r][c] != left:
                        all_same = False
                        break

                if not all_same and left not in added:
                    broken.append(left)
                    added.add(left)

        # 상하 이동
        else:
            for c in range(m):
                top = board[0][c]
                bottom = board[n - 1][c]

                if top == 0 or top != bottom:
                    continue

                # 열 전체가 같은 앱으로 꽉 차 있으면 잘린 것이 아님
                all_same = True
                for r in range(n):
                    if board[r][c] != top:
                        all_same = False
                        break

                if not all_same and top not in added:
                    broken.append(top)
                    added.add(top)

        return broken

    def process(start, direction):
        group = get_group(start, direction)
        move_group(group, direction)

        while True:
            broken = find_broken_apps(direction)

            if not broken:
                break

            next_start = broken[0]
            group = get_group(next_start, direction)
            move_group(group, direction)

    for app, direction in commands:
        process(app, direction)

    return board