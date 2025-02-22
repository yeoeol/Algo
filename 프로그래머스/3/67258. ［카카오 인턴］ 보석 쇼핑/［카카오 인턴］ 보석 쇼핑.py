def solution(gems):
    gem_types = set(gems)
    m_len = len(gem_types)
    answer = []
    left, right = 0, 0
    current_gems = {}

    while right < len(gems):
        if gems[right] in current_gems:
            current_gems[gems[right]] += 1
        else:
            current_gems[gems[right]] = 1
        right += 1

        if len(current_gems) == m_len:
            while left < right:
                if current_gems[gems[left]] > 1:
                    current_gems[gems[left]] -= 1
                    left += 1
                else:
                    break
            answer.append((left+1, right))

    answer.sort(key=lambda x: (x[1]-x[0], x[0]))
    return answer[0]