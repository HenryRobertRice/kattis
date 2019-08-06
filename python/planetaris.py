n, a = [int(x) for x in input().split()]
systems = [int(x) for x in input().split()]
systems.sort()
wins = 0
for s in systems:
    a -= (s + 1)
    if a < 0:
        break
    else:
        wins += 1
print(wins)
