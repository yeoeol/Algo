def solution(edges):
    # 8자는 중심점 제외, 모든 노드가 인, 아웃 하나씩 (중심점은 둘씩)
    # 막대는 중심점 제외, 모든 노드가 인, 아웃 하나씩 (중심점은 아웃 하나)
    # 도넛은 모든 노드가 인, 아웃 하나씩으로 자신에게 돌아옴
    answer = [0, 0, 0, 0]
    
    degree = {}
    for a, b in edges:
        if a not in degree: degree[a] = [0, 0]
        if b not in degree: degree[b] = [0, 0]
        degree[a][1] += 1
        degree[b][0] += 1
        
    for key, val in degree.items():
        i, o = val
        
        if i == 0 and o >= 2:
            answer[0] = key
        elif o == 0:
            answer[2] += 1
        elif i >= 2 and o == 2:
            answer[3] += 1
        
    total = degree[answer[0]][1]
    answer[1] = total - (answer[2]+answer[3])    
    return answer
    