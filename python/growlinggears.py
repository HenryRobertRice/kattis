def vertex_x(a, b):
    return b / (2 * a)


def vertex_y(x, a, b, c):
    return -1 * a * x ** 2 + b * x + c


def main():
    for _ in range(int(input())):
        gears = [[int(x) for x in input().split()] for i in range(int(input()))]
        max_torques = [vertex_y(vertex_x(g[0], g[1]), g[0], g[1], g[2]) for g in gears]
        print(max_torques.index(max(max_torques)) + 1)


if __name__ == "__main__":
    main()
