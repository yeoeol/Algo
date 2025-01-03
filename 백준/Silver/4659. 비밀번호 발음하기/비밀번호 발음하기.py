consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
vowel = ['a', 'e', 'i', 'o', 'u']
while True:
    pw = input()
    if pw == "end":
        break
    # 첫번째 조건
    first_flag = False
    for i in pw:
        if i in vowel:
            first_flag = True
    if not first_flag:
        print('<%s> is not acceptable.'%(pw))
        continue
    # 두번째 조건
    second_flag = True
    for i in range(len(pw)-2):
        cnt_co = 0
        cnt_vo = 0
        t = list(pw[i:i+3])
        for j in t:
            if j in consonant:
                cnt_co += 1
            elif j in vowel:
                cnt_vo += 1
        if cnt_co == 3 or cnt_vo == 3:
            second_flag = False
            break
    if not second_flag:
        print('<%s> is not acceptable.'%(pw))
        continue
    # 세번째 조건
    third_flag = True
    for i in range(97, 123):
        c = chr(i)
        if c == 'e' or c == 'o':
            continue
        if c*2 in pw:
            third_flag = False
            break
    if not third_flag:
        print('<%s> is not acceptable.'%(pw))
        continue
    print('<%s> is acceptable.'%(pw))

