while True:
    n = int(input())
    if n != 0:
        foods = dict()
        for i in range(n):
            line = input().split()
            for j in range(1, len(line)):
                #print("checking " + line[j])
                if line[j] not in foods:
                    #print("no")
                    foods[line[j]] = [line[0]]
                else:
                    #print("yes")
                    foods[line[j]].append(line[0])
        #print(str(foods))
        for food in sorted(list(foods.keys())):
            print(str(food) + " " + str(" ".join(sorted(foods[food]))))
        print()
    else:
        break
