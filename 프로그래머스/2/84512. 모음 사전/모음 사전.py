arr = ['A', 'E', 'I', 'O', 'U']
lst = []
def choose(idx, n, dic):
    if len(lst) == n:
        dic.append(list(lst))
        return

    for w in arr:
        lst.append(w)
        choose(idx+1, n, dic)
        lst.pop()

def solution(word):
    dic = []

    for i in range(1, 6):
        choose(0, i, dic)
    dic.sort()
    return dic.index(list(word))+1