d = {'R':(1, 0),
     'L':(-1, 0),
     'B':(0, -1),
     'T':(0, 1),
     'RT':(1, 1),
     'LT':(-1, 1),
     'RB':(1, -1),
     'LB':(-1, -1)
     }

king, dol, n = input().split()

for _ in range(int(n)):
    order = input()
    mx, my = d[order]
    kx, ky = chr(ord(king[0])+mx), int(king[1])+my
    if kx < 'A' or kx > 'H' or ky < 1 or ky > 8:
        continue
    if (kx == dol[0]) and (ky == int(dol[1])):
        dx, dy = chr(ord(dol[0])+mx), int(dol[1])+my
        if dx < 'A' or dx > 'H' or dy < 1 or dy > 8:
            continue
        dol = (dx, dy)
    king = (kx, ky)
print(str(king[0])+str(king[1]))
print(str(dol[0])+str(dol[1]))