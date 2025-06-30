from collections import defaultdict

t = int(input())
for _ in range(t):
    s = input()
    dic = defaultdict(int)

    i = 0
    while i < len(s):
        item = s[i]
        dic[item] += 1
        if dic[item] == 3:
            dic[item] = 0
            if i >= len(s)-1 or s[i+1] != item:
                print("FAKE")
                break
            i += 1

        i += 1

    else:
        print("OK")