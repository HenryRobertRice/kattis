from math import sqrt
def dist(bx, by, cx, cy):
    return sqrt((bx - cx) ** 2 + (by - cy) ** 2)
for i in range(input()):
    bx, by = [float(x) for x in raw_input().split()]
    candle = 0
    for j in range(input()):
        cx, cy = [float(x) for x in raw_input().split()]
        if dist(bx, by, cx, cy) <= 8.0:
            candle = 1
    if candle == 0:
        print("curse the darkness")
    else:
        print("light a candle")
