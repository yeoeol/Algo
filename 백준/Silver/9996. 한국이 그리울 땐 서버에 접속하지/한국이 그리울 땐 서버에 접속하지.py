n = int(input())
pattern = input()

for _ in range(n):
    string = input()
    pat = pattern.split("*")
    if len(string) < len(pat[0])+len(pat[1]):
        print("NE")
    elif string.startswith(pat[0]) and string.endswith(pat[1]):
        print("DA")
    else:
        print("NE")
