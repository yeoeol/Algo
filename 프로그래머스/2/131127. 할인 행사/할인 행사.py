def solution(want, number, discount):
    answer = 0

    step = 0
    while True:
        if len(discount[step:step+10]) < 10:
            break
        target = discount[step:step+10]
        for w in range(len(want)):
            if target.count(want[w]) < number[w]:
                break
        else:
            answer += 1
        step += 1

    return answer