def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x:(x[col-1], -x[0]))
    
    s = []
    for i in range(1, len(data)+1):
        _sum = 0
        for j in range(len(data[i-1])):
            _sum += data[i-1][j] % i
        s.append(_sum)
    
    ini = s[row_begin-1]
    for i in range(row_begin, row_end):
        ini ^= s[i]
    return ini
            