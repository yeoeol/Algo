def solution(str1, str2):
    lst1 = sorted(make_lst(str1))
    lst2 = sorted(make_lst(str2))
    
    # 두 리스트의 교집합 개수(중복 허용)를 세고
    # 두 리스트의 길이 합으로 나누기
    if len(lst1) == 0 and len(lst2) == 0:
        return 65536
    
    inter = make_inter(lst1, lst2)
    uni = make_union(lst1, lst2)
    
    return int(65536*(len(inter)/len(uni)))
    

# s: 두 글자씩 잘라서 리스트 만들기
# 공백, 숫자, 특수 문자가 들어 있는 경우, 버리기
# 대소문자 구분 X
def make_lst(s):
    lst = []
    for i in range(1, len(s)):
        if is_eng_char(s[i-1]) and is_eng_char(s[i]):
            w = (s[i-1]+s[i]).upper()
            lst.append(w)
    return lst

def is_eng_char(c):
    if ('a' <= c <= 'z') or ('A' <= c <= 'Z'):
        return True
    return False

def make_inter(lst1, lst2):
    inter = []
    for s in set(lst1):
        s = s.upper()
        cnt = min(lst1.count(s), lst2.count(s))
        for _ in range(cnt):
            inter.append(s)
    return inter

def make_union(lst1, lst2):
    uni = []
    for s in set(lst1):
        s = s.upper()
        cnt = max(lst1.count(s), lst2.count(s))
        for _ in range(cnt):
            uni.append(s)
            
    for s in set(lst2):
        s = s.upper()
        if s not in uni:
            cnt = lst2.count(s)
            for _ in range(cnt):
                uni.append(s)
    return uni
