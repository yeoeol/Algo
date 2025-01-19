def hash(s):
    total = 0
    for i in range(len(s)):
        total += (ord(s[i])-96)*(31**i)
    return total % 1234567891
l = int(input())
s = input()

print(hash(s))
