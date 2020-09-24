from functools import reduce
from math import gcd

def main():
    m, n = map(int, input().split())
    times = list(map(int, input().split()))
    distances = list(map(int, input().split()))
    time_ratios = get_ratios(times)
    distance_ratios = get_ratios(distances)
    possible_distances = get_possible_distances(time_ratios, distance_ratios, distances)
    print(len(possible_distances))
    possible_distances.sort()
    print(" ".join([str(x) for x in possible_distances]))


def get_ratios(distances):
    ratios = []
    for i in range(len(distances) - 1):
        ratios.append(distances[i + 1] - distances[i])
    if len(ratios) > 1:
        d = reduce(lambda r1, r2: gcd(r1, r2), ratios)
        for i in range(len(ratios)):
            ratios[i] /= d
    return ratios


def get_possible_distances(time_ratios, distance_ratios, distances):
    speeds = set()
    for i in range(len(distance_ratios) - len(time_ratios) + 1):
        if is_proportionate(time_ratios, distance_ratios[i: i + len(time_ratios)]):
            speeds.add(distances[i + 1] - distances[i])
    return list(speeds)


def is_proportionate(r1, r2):
    proportion = r2[0] / r1[0]
    for i in range(1, len(r2)):
        if r2[i] / r1[i] != proportion:
            return False
    return True


if __name__ == "__main__":
    main()
