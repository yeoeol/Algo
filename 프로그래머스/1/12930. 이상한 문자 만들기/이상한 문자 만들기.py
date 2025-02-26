def solution(s):
    splits = s.split(" ")
    lst = []
    for sp in splits:
        for i in range(len(sp)):
            if i % 2 == 0:
                lst.append(sp[i].upper())
            else:
                lst.append(sp[i].lower())
        lst.append(' ')
    answer = ''.join(lst)
    return answer[:-1]

solution("try   hello  world")