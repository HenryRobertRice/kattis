num_worlds = int(input())
worlds = [int(x) for x in input().split()]
lives = 0
for i in range(num_worlds - 2, -1, -1):
    # i - 1 already strictly less than i
    if worlds[i] < worlds[i + 1]:
        continue
    # i - 1 not strictly less than i
    else:
        diff = abs(worlds[i + 1] - worlds[i]) + 1
        worlds[i] -= diff
        lives += diff
        # check for impossibility
        if worlds[i] < 0:
            lives = 1
            break
print(str(lives))
