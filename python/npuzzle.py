def score(i, j, c, layout):
    if c == ".":
        return 0
    return abs(i - layout.get(c)[0]) + abs(j - layout.get(c)[1])
layout = {"A": (0, 0), "B": (0, 1), "C": (0, 2), "D": (0, 3),
          "E": (1, 0), "F": (1, 1), "G": (1, 2), "H": (1, 3),
          "I": (2, 0), "J": (2, 1), "K": (2, 2), "L": (2, 3),
          "M": (3, 0), "N": (3, 1), "O": (3, 2)}
board = []
for i in range(4):
    board.append(input())
total = 0
for i in range(4):
    for j in range(4):
        total += score(i, j, board[i][j], layout)
print(str(total))
