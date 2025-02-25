def solution(friends, gifts):
    # 선물지수 : 준 선물 +1, 받은 선물 -1
    # 두 사람이 선물을 주고받은 기록이 있다면,
    # 이번 달까지 두 사람 사이에 더 많은 선물을 준 사람이 다음 달에 선물을 하나 받음
    # 선물을 주고받은 기록이 없거나 수가 같다면, 선물 지수가 큰 사람 -> 작은 사람
    # 선물 지수도 같다면 주고받지 않음

    # friends 개수 크기의 2차원 배열 생성
    # 각 friend에게 번호 부여 -> dict()
    # 이후 각각의 인덱스에 맞게 gifts 배열 돌면서 개수 증가시키기 -> O(n) - 10000
    n = len(friends)
    gift_score = [0]*n
    result = [0]*n

    friend = {f: i for i, f in enumerate(friends)}

    graph = [[0]*n for _ in range(n)]
    for gift in gifts:
        a, b = gift.split(" ")
        graph[friend[a]][friend[b]] += 1

    for i in range(n):
        gift_score[i] = sum(graph[i]) - sum([k[i] for k in graph])

    # 그래프를 순회하면서 0이 아니라면 (i, j) 의 값과 (j, i)의 값을 비교해서 더 작은 수에 있는 사람이
    for i in range(n):
        for j in range(n):
            if graph[i][j] > graph[j][i]:
                # 큰 수의 사람에게 선물을 줌 (해당 사람의 come[idx] += 1)
                result[i] += 1
            elif graph[i][j] == graph[j][i]:
                if gift_score[i] > gift_score[j]:
                    result[i] += 1

    # 그래프의 (i,j) == (j, i)라면 gift_score 를 비교해서 작은 사람이 큰 사람에게 선물
        # 이때, 선물 지수까지 같다면 주고받지 않음
    return max(result)
