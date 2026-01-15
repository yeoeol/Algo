num = 1
s = input()


def solution(s):
    stack = []
    cnt = 0
    for i in range(len(s)):
        if not stack and s[i] == '}':
            cnt += 1
            stack.append("{")
        elif not stack and s[i] == '{':
            stack.append(s[i])
        elif stack and s[i] == '}':
            stack.pop()
        elif stack and s[i] == '{':
            stack.append(s[i])

    if not stack:
        return cnt
    return cnt + len(stack)//2



while '-' not in s:
    res = solution(s)
    print(f"{num}. {res}")
    num += 1
    s = input()