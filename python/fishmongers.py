num_fish, fishmongers = [int(x) for x in input().split()]
fish = [int(x) for x in input().split()]
fish.sort()
buyers = [[int(x) for x in input().split()] for _ in range(fishmongers)]
buyers.sort(key = lambda buyer: buyer[1], reverse = True)
profit = 0
for buyer in buyers:
    #get every fish he'll buy
    fish_to_buy = buyer[0]
    while fish and fish_to_buy:
        fish_to_buy -= 1
        current_fish = fish.pop()
        profit += buyer[1] * current_fish
print(str(profit))
