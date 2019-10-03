def main():
    r, c = map(int, input().split())
    rows = [input() for _ in range(r)]
    cols = [[row[i] for row in rows] for i in range(c)]
    for i, col in enumerate(cols):
        cols[i] = fall(col)
    printcols(cols, r)

def fall(col):
    newcol = []
    apples = 0
    dots = 0
    for i in range(len(col) - 1, -1, -1):
        if col[i] == 'a':
            apples += 1
        if col[i] == '.':
            dots += 1
        if col[i] == '#':
            for j in range(apples):
                newcol.append('a')
            apples = 0
            for j in range(dots):
                newcol.append('.')
            dots = 0
            newcol.append('#')
    for i in range(apples):
        newcol.append('a')
    for i in range(dots):
        newcol.append('.')
    return newcol[::-1]

def printcols(cols, r):
    rows = [[col[i] for col in cols] for i in range(r)]
    for row in rows:
        print("".join(row))

if __name__ == "__main__":
    main()
