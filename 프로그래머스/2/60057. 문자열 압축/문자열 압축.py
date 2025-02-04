def solution(s):
    m = 1001
    ss = s
    for l in range(1, len(s)+1):
        result = ""
        lst = []
        while ss != "":
            cut_ss = ss[:l]
            lst.append(cut_ss)
            ss = ss[l:]
        num = 1
        for i in range(len(lst)-1):
            if lst[i] == lst[i+1]:
                num += 1
            else:
                if num == 1:
                    result += lst[i]
                else:
                    result += str(num)+lst[i]
                    num = 1
        if num == 1:
            result += lst[-1]
        else:
            result += str(num)+lst[-1]
        m = min(m, len(result))
        ss = s
    return m