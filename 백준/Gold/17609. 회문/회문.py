t = int(input())
answer = []

def is_pal(s, i, j):
    while i < j:
        if s[i] != s[j]:
            return False
        i, j = i+1, j-1
    return True

def solution(s):
    i, j = 0, len(s)-1
    while i < j:
        if s[i] == s[j]:
            i, j = i+1, j-1
        else:
            if is_pal(s, i+1, j) or is_pal(s, i, j-1):
                return 1
            else:
                return 2
    return 0


for _ in range(t):
    s = input()
    answer.append(solution(s))
print(*answer, sep="\n")