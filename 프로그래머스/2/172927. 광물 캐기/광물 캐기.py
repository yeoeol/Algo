# 곡괭이 종류: 0=diamond, 1=iron, 2=stone
tired = [
    [1, 1, 1],      # diamond pick
    [5, 1, 1],      # iron pick
    [25, 5, 1]      # stone pick
]

dic = {"diamond":0, "iron":1, "stone":2}

def solution(picks, minerals):
    n = len(minerals)
    answer = float('inf')

    def dfs(idx, picks, fatigue):
        nonlocal answer

        # 모든 광물을 캐거나, 더 이상 곡괭이가 없으면 종료
        if idx >= n or sum(picks) == 0:
            answer = min(answer, fatigue)
            return

        # 현재까지의 피로도가 이미 최소값보다 크면 가지치기
        if fatigue >= answer:
            return

        # 곡괭이 3종류 중 하나를 선택
        for p in range(3):
            if picks[p] == 0:
                continue

            new_picks = picks[:]
            new_picks[p] -= 1

            # 이번에 p곡괭이로 캐는 피로도 계산
            add_fatigue = 0
            for k in range(idx, min(idx+5, n)):
                m = dic[minerals[k]]
                add_fatigue += tired[p][m]

            dfs(idx+5, new_picks, fatigue + add_fatigue)

    dfs(0, picks, 0)
    return answer
