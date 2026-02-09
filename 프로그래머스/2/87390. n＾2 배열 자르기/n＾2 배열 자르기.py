def solution(n, left, right):
    res = []
    for idx in range(left, right + 1):
        row = idx // n
        col = idx % n
        res.append(max(row + 1, col + 1))
        
    return res