n, k = map(int, input().split())

arr = ['']*n

idx = n-1
for _ in range(k):
    s, word = input().split()
    s = int(s)
    idx = (idx-s)%n

    if word in arr and arr[idx] != word:
        print('!')
        exit()
    if arr[idx] != '' and arr[idx] != word:
        print('!')
        exit()

    arr[idx] = word

for _ in range(n):
    print(arr[idx] if arr[idx] != '' else '?', end='')
    idx = (idx+1)%n
