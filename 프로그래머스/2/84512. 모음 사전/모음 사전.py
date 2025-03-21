arr = ['A', 'E', 'I', 'O', 'U']
lst = []
def choose(n, dic):
    if len(lst) == n:
        dic.append(''.join(lst))
        return

    for w in arr:
        lst.append(w)
        choose(n, dic)
        lst.pop()

def solution(word):
    dic = []

    for i in range(1, 6):
        choose(i, dic)
    
    return sorted(dic).index(word)+1