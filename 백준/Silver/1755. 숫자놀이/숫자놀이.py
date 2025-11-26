dic = {
    0:"zero", 1:"one", 2:"two",
    3:"three", 4:"four", 5:"five",
    6:"six", 7:"seven", 8:"eight",
    9:"nine"
}

m, n = map(int, input().split())
arr = []
for i in range(m, n+1):
    i = str(i)
    res = ""
    for num in i:
        res += dic[int(num)]
    arr.append((res, i))
arr.sort()
i = 0
for i, (_, num) in enumerate(arr):
    if i != 0 and i % 10 == 0:
        print()
    print(num, end=" ")