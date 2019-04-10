from sys import stdin

row0 = list("`1234567890-=")
row1 = list("QWERTYUIOP[]\\")
row2 = list("ASDFGHJKL;\'")
row3 = list("ZXCVBNM,./")

def main():
    for line in stdin:
        output = []
        for m in line:
            output.append(shift(m))
        output.remove(None)
        print("".join(output))

def shift(m):
    if m == " ":
        return " "
    if m in row0:
        return row0[row0.index(m) - 1]
    if m in row1:
        return row1[row1.index(m) - 1]
    if m in row2:
        return row2[row2.index(m) - 1]
    if m in row3:
        return row3[row3.index(m) - 1]

if __name__ == "__main__":
    main()
