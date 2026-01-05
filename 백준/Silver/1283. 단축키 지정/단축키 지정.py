import sys


def input():
    return sys.stdin.readline().strip()

def solution(sets, s):
    split = s.split()
    idx = 0
    flag = False
    # 단어의 첫 글자가 sets에 없다면 sets에 넣고 몇 번째 단어인지 인덱스 저장
    for i, word in enumerate(split):
        if word[0].upper() not in sets:
            idx = i
            flag = True
            break
    # 첫 번째 글자 단축키 지정
    arr = []
    if flag:
        for i, word in enumerate(split):
            if i == idx:
                sets.add(word[0].upper())
                arr.append("["+word[0]+"]"+word[1:])
            else:
                arr.append(word)
        return arr
    else:
        # 왼쪽에서부터 차례대로 알파벳 순회, 단축키로 지정안된 것이 있다면 지정
        flag = False
        for i, word in enumerate(split):
            temp = ""
            for j in range(len(word)):
                if not flag and word[j].upper() not in sets:
                    sets.add(word[j].upper())
                    temp += "["+word[j]+"]"
                    flag = True
                else:
                    temp += word[j]
            arr.append(temp)
        return arr

n = int(input())
sets = set()
for _ in range(n):
    s = input()
    print(*solution(sets, s))
