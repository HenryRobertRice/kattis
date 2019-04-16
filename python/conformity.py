combos = dict()
for i in range(int(input())):
    combo = [int(x) for x in input().split()]
    combo.sort()
    combo = str(combo)
    if combo in combos:
        combos[combo] += 1
    else:
        combos[combo] = 1
max_val = 0
for combo in combos:
    if combos[combo] > max_val:
        max_val = combos[combo]
n = 0
for combo in combos:
    if combos[combo] == max_val:
        n += combos[combo]
print(str(n))
