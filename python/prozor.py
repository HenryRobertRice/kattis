def main():
    r, s, k = map(int, input().split())
    picture = [input() for _ in range(r)]
    x, y, max_flies = 0, 0, 0
    for i in range(r):
        for j in range(s):
            temp_flies = swat(picture, i, j, k)
            if temp_flies > max_flies:
                max_flies = temp_flies
                x = i
                y = j
    print(max_flies)
    picture = new_picture(picture, x, y, k)
    for row in picture:
        print("".join(row))

def swat(picture, i, j, k):
    flies = 0
    if i + k - 1 >= len(picture) or j + k - 1 >= len(picture[0]):
        return flies
    for x in range(i + 1, i + k - 1):
        for y in range(j + 1, j + k - 1):
            if picture[x][y] == '*':
                flies += 1
                '''
                print(len(picture))
                print(len(picture[0]))
                print(i)
                print(j)
                '''
    return flies

def new_picture(picture, x, y, k):
    picture = [list(row) for row in picture]
    picture[x][y] = '+'
    picture[x + k - 1][y] = '+'
    picture[x][y + k - 1] = '+'
    picture[x + k - 1][y + k - 1] = '+'
    for j in range(y + 1, y + k - 1):
        picture[x][j] = '-'
        picture[x + k - 1][j] = '-'
    for i in range(x + 1, x + k - 1):
        picture[i][y] = '|'
        picture[i][y + k - 1] = '|'
    return picture

if __name__ == "__main__":
    main()
