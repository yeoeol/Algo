from collections import deque

dic = {
    "diamond":0,
    "iron":1,
    "stone":2
}

tired = {
    0:[1, 1, 1],
    1:[5, 1, 1],
    2:[25, 5, 1]
}


def dig(x, pos, minerals):
    res = 0
    for k in range(pos, pos+5):
        if k >= len(minerals):
            break
        cur_mineral = minerals[k]
        res += tired[x][dic[cur_mineral]]
    return res

def calc_weight(minerals):
    arr = []
    for m in range(0, len(minerals), 5):
        start = m
        end = m+5 if m+5 < len(minerals) else len(minerals)
        weight = 0
        for i in range(start, end):
            if minerals[i] == "diamond":
                weight += 25
            elif minerals[i] == "iron":
                weight += 5
            else:
                weight += 1
        arr.append((weight, start))
    return arr
    
def solution(picks, minerals):
    arr = calc_weight(minerals)
    print(arr)
    if sum(picks)*5 < len(minerals):
        arr.pop()
    arr.sort()
    
    ans = 0
    i = 0
    while i <= 2 and arr:
        if picks[i] == 0:
            i += 1
            continue
        _, start = arr.pop()
        picks[i] -= 1
        ans += dig(i, start, minerals)
    return ans