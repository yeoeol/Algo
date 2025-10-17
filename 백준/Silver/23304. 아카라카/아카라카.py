import sys
sys.setrecursionlimit(10**6)

def is_akaraka(string):
    if len(string) == 1:
        return True

    if string != string[::-1]:
        return False

    n = len(string)
    prefix = string[:n//2]

    return is_akaraka(prefix)

s = input()
if is_akaraka(s):
    print("AKARAKA")
else:
    print("IPSELENTI")