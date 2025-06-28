from collections import deque

lst = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
a = input()
b = input()

string = deque()
for i in range(len(a)):
    string.append(a[i])
    string.append(b[i])

for i in range(len(string)):
    idx = ord(string[i])-65
    string[i] = lst[idx]

while len(string) != 2:
    for i in range(len(string)-1):
        left = string.popleft()
        right = string[0]
        if left+right >= 10:
            string.append((left+right)%10)
        else:
            string.append(left+right)
    string.popleft()

print(''.join(map(str, string)))