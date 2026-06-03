def solution(skill, skill_trees):
    answer = 0

    set_skill = set(skill)
    for st in skill_trees:
        arr = []
        for c in st:
            if c in set_skill:
                arr.append(c)

        num = 0
        for s in arr:
            if s == skill[num]:
                num += 1
            else:
                break
        else:
            answer += 1
    return answer