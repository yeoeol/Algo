def solution(n, info):
    best_diff = 0
    best = [-1]

    def dfs(idx, arrows_left, lion):
        nonlocal best_diff, best

        # 11개 점수 모두 처리
        if idx == 11:
            if arrows_left > 0:
                lion[10] += arrows_left

            apeach, ryan = 0, 0
            for i in range(11):
                if info[i] == 0 and lion[i] == 0:
                    continue
                if lion[i] > info[i]:
                    ryan += (10 - i)
                else:
                    apeach += (10 - i)

            diff = ryan - apeach
            if diff > 0:
                if diff > best_diff:
                    best_diff = diff
                    best = lion[:]
                elif diff == best_diff:
                    # 낮은 점수 더 많이 맞힌 경우 우선
                    for i in range(10, -1, -1):
                        if lion[i] > best[i]:
                            best = lion[:]
                            break
                        elif lion[i] < best[i]:
                            break

            if arrows_left > 0:
                lion[10] -= arrows_left
            return

        # 1) 현재 점수를 이기는 경우
        need = info[idx] + 1
        if arrows_left >= need:
            lion[idx] = need
            dfs(idx + 1, arrows_left - need, lion)
            lion[idx] = 0

        # 2) 현재 점수를 포기하는 경우
        dfs(idx + 1, arrows_left, lion)

    dfs(0, n, [0] * 11)
    return best