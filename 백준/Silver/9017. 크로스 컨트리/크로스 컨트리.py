import sys

def input():
    return sys.stdin.readline().strip()

def find_five(arr):
    d = dict()
    c = [0 for _ in range(max(arr)+1)]
    for i, a in enumerate(arr):
        c[a] += 1
        if c[a] == 5 and a in res:
            d[a] = values[i]
    return d

T = int(input())
def find_min(scores):
    m_s = sys.maxsize
    for score in scores:
        if score != 0 and score < m_s:
            m_s = score
    return m_s


for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = [0 for _ in range(max(arr)+1)]
    scores = [0 for _ in range(max(arr)+1)]
    score_cnt = [0 for _ in range(max(arr)+1)]
    values = [0 for _ in range(n)]

    for num in arr:
        cnt[num] += 1

    score = 1
    for i, num in enumerate(arr):
        if cnt[num] == 6:
            if score_cnt[num] < 4:
                scores[num] += score
                score_cnt[num] += 1
            values[i] = score
            score += 1

    res = []
    min_score = find_min(scores)
    for i, s in enumerate(scores):
        if s == min_score:
            res.append(i)

    if len(res) == 1:
        print(res[0])
    else:
        five = find_five(arr)
        m = min(five.values())
        for key in five:
            if five[key] == m:
                print(key)

