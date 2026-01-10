def solution(k, d):
    answer = 0
    max_a = d // k

    for a in range(max_a + 1):
        remain = d*d - (a*k)*(a*k)
        if remain < 0:
            break
        max_b = int((remain ** 0.5) // k)
        answer += max_b + 1

    return answer