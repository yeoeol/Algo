a, b, c = map(int, input().split())

def div(a, b):
    if b == 1:
        return a % c
    temp = div(a, b//2)
    if b % 2 == 0:
        return (temp*temp) % c
    else:
        return ((temp*temp) * a) % c

print(div(a, b))
