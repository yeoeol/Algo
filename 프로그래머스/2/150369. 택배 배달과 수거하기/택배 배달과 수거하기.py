def solution(cap, n, deliveries, pickups):
    ans = 0
    # 재활용 택배 상자를 최대 cap개 실을 수 있음
    # 남은 배달, 남은 수거
    d_idx = n-1
    r_idx = n-1
    
    while d_idx >= 0 or r_idx >= 0:
        
        while d_idx >= 0 and deliveries[d_idx] == 0:
            d_idx -= 1
        while r_idx >= 0 and pickups[r_idx] == 0:
            r_idx -= 1
            
        if d_idx < 0 and r_idx < 0:
            break
        ans += (max(d_idx, r_idx)+1)*2
        
        # 배달
        cur = cap
        while d_idx >= 0 and cur > 0:
            give = min(deliveries[d_idx], cur)
            deliveries[d_idx] -= give
            cur -= give
            if deliveries[d_idx] == 0:
                d_idx -= 1
        
        # 수거
        cur = cap
        while r_idx >= 0 and cur > 0:
            take = min(pickups[r_idx], cur)
            pickups[r_idx] -= take
            cur -= take
            if pickups[r_idx] == 0:
                r_idx -= 1
    return ans
            
       
