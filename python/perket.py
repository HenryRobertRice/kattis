from itertools import combinations
from math import inf

def main():
    i = int(input())
    ing = [list(map(int, input().split())) for _ in range(i)]
    max_ = inf
    for j in range(1, i + 1):
        combos = combinations(ing, j)
        for c in list(combos):
            temp = perk(c)
            if temp < max_:
                max_ = temp
    print(max_)

def perk(c):
    sum_, prod_ = 0, 1
    for pair in c:
        prod_ *= pair[0]
        sum_ += pair[1]
    return abs(prod_ - sum_)

if __name__ == "__main__":
    main()
