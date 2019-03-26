for i in range(int(input())):
    ing, por, des = [int(x) for x in input().split()]
    ingredients = []
    for j in range(ing):
        ingredients.append([x for x in input().split()])
    scale = des / por
    for ingredient in ingredients:
        ingredient[1] = float(ingredient[1])
        ingredient[2] = float(ingredient[2])
        if ingredient[2] == 100.0:
            scalemain = ingredient[1] * scale
    print("Recipe # " + str(i + 1))
    for ingredient in ingredients:
        temp = scalemain * float(ingredient[2]) / 100
        print(ingredient[0] + " " + "%.1f" % temp)
    print("-" * 40)
