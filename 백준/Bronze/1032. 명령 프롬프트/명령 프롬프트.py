n = int(input())
filenames = []
for _ in range(n):
    filenames.append(input())

answer = ""
filename = filenames[0]
for i in range(len(filename)):
    flag = True
    for j in range(1, n):
        if filename[i] != filenames[j][i]:
            flag = False
    if flag:
        answer += filename[i]
    else:
        answer += "?"

print(answer)