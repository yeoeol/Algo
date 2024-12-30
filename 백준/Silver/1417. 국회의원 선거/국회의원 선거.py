n = int(input())
peoples = [int(input()) for _ in range(n)]
origin_p = peoples.pop(0)
p = origin_p
if n == 1:
    print(0)
else:
    while True:
        M = max(peoples)
        if M >= p:
            p += 1
            peoples[peoples.index(M)] -= 1
        else:
            peoples.pop(0)
            if len(peoples) == 0 or max(peoples) < p:
                break
    print(p-origin_p)
