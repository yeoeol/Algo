from collections import deque

lst = [3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,2,2,2,1,2,1,1,1,2,2,1]
n, m = map(int, input().split())
a, b = map(deque, input().split())

# 이름 섞어 넣기
string = []
while True:
    if len(a) == 0 or len(b) == 0:
        break
    string.append(a.popleft())
    string.append(b.popleft())

if len(a) == 0:
    while len(b) != 0:
        string.append(b.popleft())
else:
    while len(a) != 0:
        string.append(a.popleft())

# 초기 상태로 만들기
for i in range(len(string)):
    idx = ord(string[i])-65
    string[i] = lst[idx]

# 반복 수행
while len(string) != 2:
    temp = []
    for i in range(len(string)-1):
        temp.append((string[i] + string[i+1])%10)
    string = temp

print(str(int(''.join(map(str, string))))+'%')