def solution(scores):
    wanho = scores[0]
    wanho_sum = sum(wanho)

    scores.sort(key=lambda x:(-x[0], x[1]))

    max_second = 0
    rank = 1

    for a, b in scores:
        if b < max_second:
            # 탈락 대상
            if [a, b] == wanho:
                return -1
            continue
            
        if a+b > wanho_sum:
            rank += 1
        
        max_second = max(max_second, b)
    
    return rank

