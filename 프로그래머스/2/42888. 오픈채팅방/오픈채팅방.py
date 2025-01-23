def solution(record):
    order = []
    dic = {}
    for r in record:
        s = r.split()
        if s[0] == "Enter":
            dic[s[1]] = s[2]
            order.append((s[0], s[1]))
        elif s[0] == "Leave":
            order.append((s[0], s[1]))
        else: # s[0] == "Change"
            dic[s[1]] = s[2]
    answer = []
    for o, u in order:
        if o == "Enter":
            answer.append(dic[u]+"님이 들어왔습니다.")
        elif o == "Leave":
            answer.append(dic[u]+"님이 나갔습니다.")

    return answer