width, height = map(int, input().split())
piece = [[0]*width for _ in range(height)]

w = [0, width]
h = [0, height]
n = int(input())
for _ in range(n):
    flag, num = map(int, input().split())
    if flag == 0:
        h.append(num)
    elif flag == 1:
        w.append(num)

w.sort()
h.sort()

M_width = M_height = 0
for i in range(1, len(w)):
    M_width = max(M_width, w[i]-w[i-1])

for i in range(1, len(h)):
    M_height = max(M_height, h[i]-h[i-1])

print(M_width*M_height)