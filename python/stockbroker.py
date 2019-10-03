def main():
    d = int(input())
    days = [int(input())]
    for i in range(d - 1):
        temp = int(input())
        if temp != days[-1]:
            days.append(temp)
    if len(days) == 1:
        print(100)
        return
    money = 100
    shares = 0
    for i in range(len(days)):
        if is_local_minimum(i, days):
            money, shares = buy_all(money, shares, days[i])
        elif is_local_maximum(i, days):
            money, shares = sell_all(money, shares, days[i])
    print(money)

def is_local_minimum(i, days):
    if i == 0 and days[i + 1] > days[i]:
            return True
    elif i > 0 and i < len(days) - 1 and days[i - 1] > days[i] and days[i + 1] > days[i]:
        return True
    return False

def is_local_maximum(i, days):
    if i == len(days) - 1 and days[i] > days[i - 1]:
        return True
    elif i > 0 and i < len(days) - 1 and days[i - 1] < days[i] and days[i + 1] < days[i]:
        return True
    return False

def buy_all(money, shares, price):
    shares_purchasable = money // price
    if shares + shares_purchasable > 100000:
        shares_purchasable = 100000 - shares
    shares += shares_purchasable
    money -= shares_purchasable * price
    return money, shares

def sell_all(money, shares, price):
    money += shares * price
    return money, 0

if __name__ == "__main__":
    main()
