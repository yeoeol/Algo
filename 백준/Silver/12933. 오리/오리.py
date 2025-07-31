duck = input()
n = len(duck)
if len(duck) % 5 != 0:
    print(-1)
    exit()

order = "quack"
cnt = 0
arr = []
ans = -1
for d in duck:
    idx = order.find(d)
    if idx == -1:
        print(-1)
        break

    if order[idx] == 'q':
        arr.append(0)
    else:
        for i in range(len(arr)):
            if arr[i]+1 == idx:
                if idx == 4:
                    arr.pop(i)
                else:
                    arr[i] += 1
                break
        else:
            ans = -1
            break

    ans = max(ans, len(arr))
if arr:
    print(-1)
else:
    print(ans)