def solution(book_time):
    book = []
    for start, end in book_time:
        s, e = map(int, start.split(':'))
        start = s*60+e
        s, e = map(int, end.split(':'))
        end = s*60+e
        book.append([start, end])
    book.sort(key=lambda x:x[0])
    print(book)

    answer = [book[0]]
    for i in range(1, len(book)):
        if len(answer) == 0:
            answer.append(book[i])
            continue
        for j in range(len(answer)):
            if answer[j][1]+10 <= book[i][0]:
                answer.pop(j)
                answer.append(book[i])
                break
        else:
            answer.append(book[i])
    return len(answer)