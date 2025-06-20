n, d = map(int, input().split())
lst = []
for i in range(1, n+1):
    lst.extend((str(i)))

print(lst.count(str(d)))