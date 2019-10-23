prev_position = 20
position = 20
down = 1
ignore = input()
plays = list(map(int, input().split()))
done = False
for p in plays:
    position += p
    if position <= 0:
        print("Safety")
        done = True
        break
    elif position >= 100:
        print("Touchdown")
        done = True
        break
    else:
        if position - prev_position >= 10:
            down = 1
            prev_position = position
        else:
            down += 1
        if down > 4:
            print("Nothing")
            done = True
            break
if not done:
    print("Nothing")
