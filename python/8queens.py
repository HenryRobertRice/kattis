from sys import exit
def attack (q1, q2):
    #same x, same y, or x1 - x2 = y1 - y2
    x = abs(q1[0] - q2[0])
    y = abs(q1[1] - q2[1])
    if x == 0 or y == 0 or x == y:
        return True
queens = []
for i in range(8):
    line = input()
    for j in range(8):
        if line[j] == "*":
            queens.append([i, j])
if len(queens) != 8:
    print("invalid")
    exit()
for i in range(7):
    for j in range(i + 1, 8):
        if attack(queens[i], queens[j]):
            print("invalid")
            exit()
print("valid")
