def main():
    r, c = map(int, input().split())
    grid = [input() for _ in range(r)]
    i, j = 0, 0
    visited = set()
    dirs = {
        "N": [-1, 0],
        "S": [1, 0],
        "W": [0, -1],
        "E": [0, 1]
    }
    steps = 0
    char = grid[i][j]
    while char != "T":
        i += dirs[char][0]
        j += dirs[char][1]
        steps += 1
        if not in_grid(i, j, r, c):
            print("Out")
            return
        char = grid[i][j]
        if (i, j) in visited:
            print("Lost")
            return
        visited.add((i, j))
    print(steps)


def in_grid(i, j, r, c):
    return 0 <= i and i < r and 0 <= j and j < c



if __name__ == "__main__":
    main()
