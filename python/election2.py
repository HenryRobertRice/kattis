candidates = dict()

for _ in range(int(input())):
    name = input()
    party = input()
    candidates[(name, party)] = 0

for _ in range(int(input())):
    name = input()
    for candidate in candidates:
        if candidate[0] == name:
            candidates[(candidate[0], candidate[1])] += 1

parties = [[candidate[1], candidates[candidate]] for candidate in candidates]
parties.sort(key=lambda party: party[1], reverse=True)

if parties[0][1] == parties[1][1]:
    print("tie")
else:
    print(parties[0][0])
