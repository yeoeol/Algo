import itertools

def solution(k, dungeons):
    lst = list(itertools.permutations(dungeons, len(dungeons)))

    def find(remain, l):
        answer = 0
        for i in range(len(l)):
            req = l[i][0]
            ex = l[i][1]
            if req <= remain:
                remain -= ex
                answer += 1
        return answer

    result = -1
    for i in range(len(lst)):
        result = max(result, find(k, lst[i]))

    return result