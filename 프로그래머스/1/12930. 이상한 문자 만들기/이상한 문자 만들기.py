def solution(s):
    answer = ''
    splits = s.split(" ")
    for sp in splits:
        lst = []
        for i in range(len(sp)):
            if i % 2 == 0:
                lst.append(sp[i].upper())
            else:
                lst.append(sp[i].lower())
        answer += ''.join(lst)+" "
        
    return answer[:-1]

solution("try   hello  world")