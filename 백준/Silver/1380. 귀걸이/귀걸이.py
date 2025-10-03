scenario_cnt = 1
n = int(input())
while n != 0:
    names = dict()
    for i in range(1, n+1):
        names[i] = input()

    seize = dict()
    for _ in range(2*n-1):
        num, ab = input().split()
        if num not in seize:
            seize[num] = ab
        else:
            del seize[num]
    print(scenario_cnt, names[int(list(seize.keys())[0])])
    scenario_cnt += 1
    
    n = int(input())
