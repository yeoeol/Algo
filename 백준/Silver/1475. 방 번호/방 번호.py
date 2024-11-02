s = input()
lst = [0] * 9

for i in list(s):
    if int(i) == 6 or int(i) == 9:
        lst[6] += 1
    else:
        lst[int(i)] += 1

M = max(lst)
c = lst.count(M)
if len(s) == 1:
    print(M)
elif len(s) != 0 and M == lst[6] and c == 1:
    if M % 2 == 0:
        print(M//2)
    else:
        print(M//2+1)
else:
    print(M)
