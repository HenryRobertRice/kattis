words = set()
result = 0
for i in range(int(input())):
    if i == 0:
        prev = input()
        words.add(prev)
    else:
        curr = input()
        if curr[0] == prev[-1] and curr not in words:
            words.add(curr)
            prev = curr
        else:
            if result == 0:
                if i % 2 == 0:
                    result = 1
                else:
                    result = 2
if result == 0:
    print("Fair Game")
else:
    print("Player " + str(result) + " lost")
