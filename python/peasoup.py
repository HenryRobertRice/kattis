def main():
    n = int(input())
    restaurants = []
    for i in range(n):
        k = int(input())
        name = input()
        items = set()
        for j in range(k):
            items.add(input())
        restaurants.append([name, items])
    for i in range(len(restaurants)):
        if "pea soup" in restaurants[i][1] and "pancakes" in restaurants[i][1]:
            print(restaurants[i][0])
            return
    print("Anywhere is fine I guess")

if __name__ == "__main__":
    main()
