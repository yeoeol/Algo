import heapq

def solution(jobs):
    wait_queue = []
    n = len(jobs)
    total_wait_time = 0
    # 작업의 소요시간이 짧은 것
    # 작업의 요청 시각이 빠른 것
    # 작업의 번호가 작은 것 순으로 우선순위
    time = 0
    while jobs or wait_queue:
        jobs.sort(key=lambda x:x[0])
        while jobs:
            t, cost = jobs[0]
            if t > time:
                break
            jobs.pop(0)
            heapq.heappush(wait_queue, (cost, t))
        if wait_queue:
            duration, strat = heapq.heappop(wait_queue)
            time += duration
            total_wait_time += time-strat
        else:
            time = jobs[0][0]

    return total_wait_time//n