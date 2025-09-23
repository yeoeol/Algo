cash = int(input())
stock_prices = list(map(int, input().split()))

def calc(c, s, n):
    return c+s*n

def jun():
    jun_cash = cash
    cnt = 0
    for price in stock_prices:
        q = jun_cash//price
        if q == 0:
            continue
        cnt += q
        jun_cash -= price*q

    return calc(jun_cash, stock_prices[-1], cnt)

def sung():
    sung_cash = cash
    cnt = 0

    flag_up, flag_down = False, False
    for i, price in enumerate(stock_prices):
        if is_up_for_three_days(i) and not flag_up and not flag_down:
            flag_up = True
            continue
        elif is_down_for_three_days(i) and not flag_up and not flag_down:
            flag_down = True
            continue

        if flag_up:
            sung_cash += price*cnt
            cnt = 0
            flag_up = False
        elif flag_down:
            if price <= sung_cash:
                q = sung_cash//price
                if q == 0:
                    continue
                cnt += q
                sung_cash -= price*q
            flag_down = False

    return calc(sung_cash, stock_prices[-1], cnt)

def is_up_for_three_days(idx):
    if idx < 2:
        return False
    for i in range(idx, idx-2, -1):
        if stock_prices[i-1] >= stock_prices[i]:
            return False
    return True

def is_down_for_three_days(idx):
    if idx < 2:
        return False
    for i in range(idx, idx-2, -1):
        if stock_prices[i-1] <= stock_prices[i]:
            return False
    return True

junhyeon = jun()
sungmin = sung()
if junhyeon > sungmin:
    print("BNP")
elif junhyeon < sungmin:
    print("TIMING")
else:
    print("SAMESAME")



