n, m = map(int, input().split())

dic = dict()
for _ in range(n):
    juso, pw = input().split()
    dic[juso] = pw

for _ in range(m):
    juso = input()
    print(dic[juso])