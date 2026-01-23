from collections import defaultdict
from bisect import bisect_left

def solution(info_lst, query):
    info_dict = defaultdict(list)

    for info in info_lst:
        splits = info.split(" ")
        cond, score = splits[:4], int(splits[-1])
        for mask in range(16):
            key = []
            for i in range(4):
                if mask & (1 << i):
                    key.append('-')
                else:
                    key.append(cond[i])
            info_dict[' '.join(key)].append(score)
    for k in info_dict:
        info_dict[k].sort()
        
    answer = []
    for q in query:
        splits = q.split(" and ")
        s = splits[-1].split()
        a, score = s[0], int(s[1])
        cond = splits[:3]
        key = ' '.join(cond)+' '+a
        lst = info_dict[key]
        answer.append(len(lst) - bisect_left(lst, score))
        # left, right = 0, len(lst)-1
        # while left < right:
        #     mid = (left+right)//2
        #     if lst[mid] < score:
        #         left = mid+1
        #     else:
        #         right = mid
        # answer.append(len(lst)-left)
    return answer

