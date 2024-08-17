def solution(s):
    answer = []

    s = s.split(' ')
    for i in s:
        answer.append(i.capitalize())

    return ' '.join(answer)