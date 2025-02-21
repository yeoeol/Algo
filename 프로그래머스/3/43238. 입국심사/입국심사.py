# t 시간 동안 심사할 수 있는 사람 수 계산
def count(times, t):
    cnt = 0
    for time in times:
        cnt += t//time
    return cnt


def solution(n, times):
    answer = 0

    m_time = min(times)
    M_time = max(times)*n

    left, right = m_time, M_time
    while left <= right:
        mid = (left+right)//2
        cnt = count(times, mid)

        if n <= cnt:
            answer = mid
            right = mid-1
        else:
            left = mid+1
    return answer