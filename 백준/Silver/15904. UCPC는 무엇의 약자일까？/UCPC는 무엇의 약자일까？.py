ucpc = ['U', 'C', 'P', 'C']

def func(string):
    idx = 0
    for i in range(len(string)):
        if string[i] == ucpc[idx]:
            idx += 1
            if idx == 4:
                return True
    return False

if func(input()):
    print("I love UCPC")
else:
    print("I hate UCPC")