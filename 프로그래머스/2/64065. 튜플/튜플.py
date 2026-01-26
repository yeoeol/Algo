def solution(s):
    s1 = s.lstrip('{').rstrip('}').split("},{")
    arr = [list(map(int, i.split(","))) for i in s1]
    arr.sort(key=len)
    
    res = []
    for items in arr:
        for i in range(len(items)):
            if items[i] not in res:
                res.append(items[i])
                break
        
    return res
        