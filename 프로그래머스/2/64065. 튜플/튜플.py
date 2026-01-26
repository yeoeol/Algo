def solution(s):
    arr = s[2:len(s)-2].split("},{")
    for i, items in enumerate(arr):
        arr[i] = list(map(int, items.split(",")))
    arr.sort(key=lambda x:len(x))
    
    sets = set()
    res = []
    n = len(arr)
    for i in range(n):
        sets2 = set(arr[i])
        p = (sets2-sets).pop()
        res.append(p)
        sets.add(p)
        
    return res
        