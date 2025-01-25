board = []
result = 0
for i in range(8):
    lst = list(input())

    if i % 2 == 0:
        for j in [0,2,4,6]:
            if lst[j] == 'F':
                result += 1
    else:
        for j in [1,3,5,7]:
            if lst[j] == 'F':
                result += 1
print(result)