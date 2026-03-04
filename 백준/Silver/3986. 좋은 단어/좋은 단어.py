n = int(input())
ans = 0


def is_good(word):
    stack = []
    for c in word:
        if not stack:
            stack.append(c)
        elif stack[-1] == c:
            stack.pop()
        elif stack[-1] != c:
            stack.append(c)
    if stack:
        return False
    return True

for _ in range(n):
    word = input()
    if is_good(word):
        ans += 1
print(ans)