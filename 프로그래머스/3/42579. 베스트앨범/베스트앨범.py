def solution(genres, plays):
    answer = []
    dic = dict()
    sum_dic = dict()
    zi = zip(genres, plays)
    for i, z in enumerate(zi):
        genre = z[0]
        play = z[1]
        if genre in dic:
            dic[genre].append((play, i))
        else:
            dic[genre] = [(play, i)]
        if genre in sum_dic:
            sum_dic[genre] += play
        else:
            sum_dic[genre] = play

    for d in dic:
        dic[d].sort(key=lambda x:x[0], reverse=True)
    while dic:
        M = max(sum_dic.values())
        M_genre = ''
        for g in sum_dic:
            if sum_dic[g] == M:
                M_genre = g
        sum_dic.pop(M_genre)
        p = dic.pop(M_genre)
        for i in p[:2]:
            answer.append(i[1])

    return answer
