def solution(band, health, attacks):
    cur_health = health
    
    # 몬스터에게 맞으면 0으로 초기화
    band_t = 0
    
    # 현재 체력
    cur_health = health
    
    # 최대 버텨야 하는 시간(마지막 공격)
    max_t = attacks[-1][0]
    
    # 전체 시간이 attacks[0][0]과 같다면, cur_health 에서 attacks[0][1] 를 빼는데, 체력이 0 이하가 된다면 return -1
    # 1초가 지날 때마다 힐링(band_t+=1, cur_health 증가, band_t가 시전 시간과 같다면 band[2] 만큼 추가 회복)
    for t in range(1, max_t+1):
        if t == attacks[0][0]:
            _, damage = attacks.pop(0)
            cur_health -= damage
            band_t = 0
            if cur_health <= 0:
                return -1
            continue
        band_t += 1
        cur_health += band[1]
        if band_t == band[0]:
            cur_health += band[2]
            band_t = 0
        if cur_health > health:
            cur_health = health
            
    return cur_health
    
