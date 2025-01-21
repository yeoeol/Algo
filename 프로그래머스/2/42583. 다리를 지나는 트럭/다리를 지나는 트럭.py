from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0]*bridge_length)
    time = 0
    i = 0
    _sum = 0
    while bridge:
        time += 1
        p = bridge.popleft()
        _sum -= p
        if truck_weights:
            if _sum+truck_weights[i] <= weight:
                bridge.append(truck_weights[i])
                _sum += truck_weights[i]
                i += 1
                if i == len(truck_weights):
                    break
            else:
                bridge.append(0)
    time += len(bridge)
    return time