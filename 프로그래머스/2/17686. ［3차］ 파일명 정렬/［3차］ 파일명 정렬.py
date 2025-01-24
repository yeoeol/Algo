def solution(files):
    answer = []
    HN = []
    for i in range(len(files)):
        file = files[i]
        ind = 0
        head = ""; number = ""
        for j in range(len(file)):
            if file[j].isnumeric():
                head = file[:j]
                ind = j
                break
        print(file)
        print(ind)
        for j in range(ind+1, len(file)):
            if (j-ind) >= 5 or not file[j].isnumeric():
                number = file[ind:j]
                break
        else:
            number = file[ind:]
        HN.append((i, head, number))
    HN.sort(key=lambda x: (x[1].upper(), int(x[2])))
    for h in HN:
        answer.append(files[h[0]])

    return answer