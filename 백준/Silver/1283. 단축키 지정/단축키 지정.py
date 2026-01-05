import sys


def input():
    return sys.stdin.readline().strip()

def solution(sets, s):
    split = s.split()
    arr = []
    # 단어의 첫 글자가 sets에 없다면 단축키 지정
    for i, word in enumerate(split):
        if word[0].upper() not in sets:
            for j, w in enumerate(split):
                if i == j:
                    sets.add(w[0].upper())
                    arr.append("["+w[0]+"]"+w[1:])
                else:
                    arr.append(w)
            return arr

    # 왼쪽에서부터 차례대로 알파벳 순회, 단축키로 지정안된 것이 있다면 지정
    for i, word in enumerate(split):
        for j in range(len(word)):
            if word[j].upper() not in sets:
                for k, w in enumerate(split):
                    if i == k:
                        sets.add(w[j].upper())
                        arr.append(w[:j] + "["+w[j]+"]" + w[j+1:])
                    else:
                        arr.append(w)
                return arr
    return [s]

n = int(input())
sets = set()
for _ in range(n):
    s = input()
    print(*solution(sets, s))
