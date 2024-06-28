n = int(input())
city_length = list(map(int, input().split()))
price = list(map(int, input().split()))

# 자신보다 오른쪽에 있는 것들 중에 리터당 가격이 더 싼 것이 있으면 거기까지 가는 길이만큼만 충전
# 더 싼 것이 없다면 현재 위치에서 남은 길이 모두 충전
# 더 비싼 것을 찾았다면 그동안의 길이만큼 현재의 위치에서 충전

p = price[0]
charge = 0
for i in range(1, n-1):
    charge += city_length[i-1]*p
    if p > price[i]:
        p = price[i]
        
charge += city_length[-1]*p
print(charge)