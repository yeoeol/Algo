def solution(genres, plays):
    answer = []
    dic = dict()
    sum_dic = dict()
    for i, (genre, play) in enumerate(zip(genres, plays)):
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
    print(dic)
    while dic:
        M_genre = max(sum_dic, key=sum_dic.get)
        sum_dic.pop(M_genre)
        p = dic.pop(M_genre)
        answer.extend([i[1] for i in p[:2]])

    return answer
