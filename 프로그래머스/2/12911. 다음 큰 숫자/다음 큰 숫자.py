def solution(n):
    cnt = bin(n).count('1')
    while True:
        n += 1
        c = bin(n).count('1')
        if c == cnt:
            break
    return n