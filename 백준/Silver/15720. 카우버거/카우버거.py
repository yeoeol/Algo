b, c, d = map(int, input().split())
prices = list(map(int, input().split()))
sides = list(map(int, input().split()))
beverages = list(map(int, input().split()))
prices.sort()
sides.sort()
beverages.sort()
print(sum(prices) + sum(sides) + sum(beverages))
ans = 0
while prices and sides and beverages:
    ans += (prices.pop() + sides.pop() + beverages.pop())*0.9
ans += sum(prices) + sum(sides) + sum(beverages)
print(int(ans))