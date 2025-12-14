from itertools import product


dis = [0.1, 0.2, 0.3, 0.4]

def make_price(lst, emoticons):
    arr = []
    for discount_percent, value in zip(lst, emoticons):
        arr.append(((1-discount_percent)*value, discount_percent*100))
    return arr

def solution(users, emoticons):
    arr = []
    for dis_lst in product(dis, repeat=len(emoticons)):
        reg = 0
        res = 0
        prices = make_price(dis_lst, emoticons)
        for k in range(len(users)):
            emo_sum = 0
            for price, percent in prices:
                # 할인율이 이상이라면 구매
                if users[k][0] <= percent: 
                    emo_sum += price
            if emo_sum >= users[k][1]:
                reg += 1
            else:
                res += emo_sum
        # 결과를 리스트에 저장
        arr.append([reg, int(res)])
    arr.sort()
    # 리스트에서 reg가 가장 큰걸 선택, 같은게 있다면 res가 가장 큰걸 선택
    return arr[-1]