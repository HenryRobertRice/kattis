def find(parents, i):
    if parents[i] == i:
        return i
    parents[i] = find(parents, parents[i])
    return parents[i]

def union(parents, i, j):
    parents[find(parents, j)] = find(parents, i)

def main():
    r, c = map(int, input().split())
    world = [input() for _ in range(r)]
    parents = [i for i in range(r * c)]
    for i in range(r):
        for j in range(c):
            if j < c - 1 and world[i][j] == world[i][j + 1]:
                union(parents, i * c + j, i * c + j + 1)
            if i < r - 1 and world[i][j] == world[i + 1][j]:
                union(parents, i * c + j, (i + 1) * c + j)
    n = int(input())
    for _ in range(n):
        r1, c1, r2, c2 = map(coord, input().split())
        if(find(parents, r1 * c + c1) == find(parents, r2 * c + c2)):
            if world[r1][c1] == '0':
                print("binary")
            else:
                print("decimal")
        else:
            print("neither")

def coord(x):
    return int(x) - 1

if __name__ == "__main__":
    main()

