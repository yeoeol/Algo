def solution(players, m, k):
    ans = 0
    cur_server = 0
    
    servers = dict()
    # players 배열 순회, 수를 m으로 나눴을 때의 개수를 need_server
    # need_server-cur_server 만큼 증설한 후, 이들은 k 시간이 지나면 삭제
    # need_server-cur_server 가 증설 횟수
    for t, num in enumerate(players):
        if t-k in servers:
            cur_server -= servers[t-k]
            del servers[t-k]
        # 해당 시각에 살아있는 서버의 수
        cur_server = sum(servers.values())
        # 해당 시각에 필요한 서버의 수
        need_server = num//m
        # 추가로 필요한 서버의 수
        inc_cnt = need_server-cur_server
        
        # 추가로 필요한 서버가 0보다 작거나 같으면 스킵
        if inc_cnt <= 0:
            continue
            
        servers[t] = inc_cnt
        ans += inc_cnt
    return ans
        