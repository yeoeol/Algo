n = int(input())
target = sorted(input())
alpha = [chr(i) for i in range(65, 91)]
answer = 0
for _ in range(n-1):
    s = sorted(input())
    # 같은 구성
    if target == s:
        answer += 1
        continue

    # 하나의 문자를 다른 문자로 바꾸어서 같은 구성
    if len(target) == len(s):
        for i in range(len(s)):
            flag = False
            temp = s[i]
            for al in alpha:
                s[i] = al
                if sorted(s) == target:
                    flag = True
                    answer += 1
                    break
            if flag:
                break
            s[i] = temp
    else:
        for al in alpha:
            # 한 단어에서 한 문자를 더하기
            a, b = [], []
            if len(target) > len(s):
                a = sorted(s+[al])
            else: # len(target) < len(s)
                b = sorted(target+[al])
            if target == a or b == s:
                answer += 1
print(answer)

