def change(n, k):
    res = ""
    while n != 0:
        res = str(n % k)+res
        n //= k
    return res

def is_prime(x):
    if x == 1:
        return False
    end = int(x**0.5)
    for i in range(2, end+1):
        if x % i == 0:
            return False
    return True

def solution(n, k):
    # n을 k진수로 변환
    n = change(n, k)
    print(n)
    ans = 0
    for num in n.split("0"):
        if num != '':
            num = int(num)
            if is_prime(num):
                ans += 1
    return ans
