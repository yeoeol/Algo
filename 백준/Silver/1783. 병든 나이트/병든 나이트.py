n, m = map(int, input().split())

def find_answer():
    if n == 1:
        return 1
    elif n == 2:
        return min((m+1)//2, 4)
    elif n >= 3:
        if m < 7:
            return min(4, m)
        else:
            return m-2

print(find_answer())