import sys
sys.setrecursionlimit(10**6)

def solution(k, room_number):
    # 방 배정 문제
    # 호텔에는 방이 총 k개(1번부터 k번까지) 있음
    result = []
    # 사람이 있으면 True, 없으면 False
    parent = dict()
    
    def find(x):
        if x not in parent:
            parent[x] = x+1
            return x
        
        parent[x] = find(parent[x])
        return parent[x]
    
    def union(a, b):
        p_a = find(a)
        p_b = find(b)
        
        if p_a < p_b:
            parent[p_b] = p_a
        else:
            parent[p_a] = p_b
    
    for room in room_number:
        result.append(find(room))
            
        # else:
            # union(room, r)
    
    return result