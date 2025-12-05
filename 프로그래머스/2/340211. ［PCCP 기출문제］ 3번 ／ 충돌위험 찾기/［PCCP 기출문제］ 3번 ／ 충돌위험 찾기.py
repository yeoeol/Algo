from collections import Counter

def get_path(start, end):
    path = []
    r1, c1 = start
    r2, c2 = end

    cur_r, cur_c = r1, c1

    # r 좌표(행) 먼저 이동 (위/아래)
    while cur_r != r2:
        if cur_r < r2:
            cur_r += 1
        else:
            cur_r -= 1
        path.append((cur_r, cur_c))

    # c 좌표(열) 나중에 이동 (좌/우)
    while cur_c != c2:
        if cur_c < c2:
            cur_c += 1
        else:
            cur_c -= 1
        path.append((cur_r, cur_c))

    return path

def solution(points, routes):
    # 각 로봇의 전체 이동 경로를 저장할 리스트
    robot_paths = []

    for route in routes:
        full_path = []
        # 시작점 추가
        start_idx = route[0] - 1
        start_pt = (points[start_idx][0], points[start_idx][1])
        full_path.append(start_pt)

        # 경유지 순서대로 경로 생성
        for i in range(len(route) - 1):
            start = points[route[i] - 1]
            end = points[route[i+1] - 1]

            # start -> end 경로 생성 (시작점 제외하고 이동 경로만 받아옴)
            segment = get_path(start, end)
            full_path.extend(segment)

        robot_paths.append(full_path)

    ans = 0
    # 모든 로봇 중 가장 긴 경로의 길이
    max_len = max(len(p) for p in robot_paths)

    # 시간 별로 충돌 확인
    for t in range(max_len):
        # t 시간에 각 로봇의 위치를 모음
        positions = []
        for path in robot_paths:
            # 이 로봇이 아직 이동 중이라면 (t가 경로 길이보다 작으면)
            if t < len(path):
                positions.append(path[t])

        # 충돌 계산 (같은 좌표에 2개 이상 있는지)
        count = Counter(positions)
        for pos, cnt in count.items():
            if cnt >= 2:
                ans += 1

    return ans