def solution(data, ext, val_ext, sort_by):
    dic = {
        "code":0,
        "date":1,
        "maximum":2,
        "remain":3
    }
    arr = []
    for i in range(len(data)):
        if data[i][dic[ext]] < val_ext:
            arr.append(data[i])
    arr.sort(key=lambda x:x[dic[sort_by]])
    return arr