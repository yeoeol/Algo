T = int(input())
for _ in range(T):
    n, k, t, m = map(int, input().split())

    submit_cnt = [0 for _ in range(n+1)]
    submit_time = [0 for _ in range(n+1)]
    problems = [[0]*(k+1) for _ in range(n+1)]
    for time in range(m):
        team_id, num, score = map(int, input().split())
        problems[team_id][num] = max(problems[team_id][num], score)
        submit_cnt[team_id] += 1
        submit_time[team_id] = time

    res = sorted([(sum(problems[i]), -submit_cnt[i], -submit_time[i], i) for i in range(1, n+1)], reverse=True)
    for i in range(len(res)):
        if res[i][3] == t:
            print(i+1)
            break
