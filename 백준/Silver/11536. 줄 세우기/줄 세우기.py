n = int(input())
names = [input() for _ in range(n)]
inc = sorted(names)
dec = sorted(names, reverse=True)
if names == inc:
    print("INCREASING")
elif names == dec:
    print("DECREASING")
else:
    print("NEITHER")