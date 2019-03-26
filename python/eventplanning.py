participants, budget, hotels, weeks = [int(x) for x in raw_input().split()]
min_cost = float("inf")
for i in range(hotels):
    price = input()
    week_list = [int(x) for x in raw_input().split()]
    for week in week_list:
        if week >= participants:
            cost = participants * price
            if cost < min_cost:
                min_cost = cost
            break
if min_cost < budget:
    print(min_cost)
else:
    print("stay home")
