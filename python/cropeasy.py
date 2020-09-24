from itertools import combinations


def main():
    for i in range(int(input())):
        print(f"Case #{i + 1}: {process(input())}")


def process(input_string):
        input_ints = [int(x) for x in input_string.split()]
        points = get_points(input_ints)
        triangles = combinations(points, 3)
        valid_triangles = 0
        for t in triangles:
            valid_triangles += is_valid_triangle(t)
        return valid_triangles


def is_valid_triangle(t):
    x = sum([t[i][0] for i in range(3)]) / 3
    y = sum([t[i][1] for i in range(3)]) / 3
    return int(x == int(x) and y == int(y))


def get_points(input_ints):
    points = []
    x = input_ints[5]
    y = input_ints[6]
    points.append((x, y))
    for i in range(1, input_ints[0]):
        x = (input_ints[1] * x + input_ints[2]) % input_ints[7]
        y = (input_ints[3] * y + input_ints[4]) % input_ints[7]
        points.append((x, y))
    return points


if __name__ == "__main__":
    main()
