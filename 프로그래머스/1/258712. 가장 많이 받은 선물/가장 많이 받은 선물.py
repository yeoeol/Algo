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
    index = dict()
    name = dict()
    gift_score = dict()
    come = dict()
    for i, f in enumerate(friends):
        index[f] = i
        name[i] = f
        gift_score[f] = 0
        come[f] = 0

    graph = [[0]*n for _ in range(n)]
    for gift in gifts:
        splits = gift.split(" ")
        s = splits[0]
        s1 = splits[1]

        a = index[splits[0]]
        b = index[splits[1]]
        graph[a][b] += 1

    for i in range(n):
        for j in range(n):
            gift_score[name[i]] -= graph[j][i]
        gift_score[name[i]] += sum(graph[i])

    print(gift_score)
    print('--------------------')
    # 그래프를 순회하면서 0이 아니라면 (i, j) 의 값과 (j, i)의 값을 비교해서 더 작은 수에 있는 사람이
    for i in range(n):
        for j in range(n):
            if graph[i][j] < graph[j][i]:
                # 큰 수의 사람에게 선물을 줌 (해당 사람의 come[idx] += 1)
                come[name[j]] += 1
            elif graph[i][j] > graph[j][i]:
                come[name[i]] += 1
            else:
                if gift_score[name[i]] < gift_score[name[j]]:
                    come[name[j]] += 1
                elif gift_score[name[i]] > gift_score[name[j]]:
                    come[name[i]] += 1
    # 그래프의 (i,j) == (j, i)라면 gift_score 를 비교해서 작은 사람이 큰 사람에게 선물
        # 이때, 선물 지수까지 같다면 주고받지 않음
    return max(come.values())//2