self_number = [False]*11000

for i in range(1, 10001):
    self_number[sum(list(map(int, list(str(i)))))+i] = True

for i in range(1, 10001):
    if not self_number[i]:
        print(i)
