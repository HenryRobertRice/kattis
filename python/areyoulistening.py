from math import sqrt, floor
def main():
    cx, cy, n = [int(x) for x in input().split()]
    devices = [[int(x) for x in input().split()] for i in range(n)]
    distances = [[dist(cx, cy, devices[i][0], devices[i][1], devices[i][2]), devices[i][2]] for i in range(len(devices))]
    distances.sort(key=lambda d: d[0])
    if distances[2][0] < 0:
        print("0")
    else:
        print(distances[2][0])
            

def dist(x1, y1, x2, y2, r):
    return floor(sqrt(abs((x1 - x2) ** 2 + (y1 - y2) ** 2)) - r)

if __name__ == "__main__":
    main()
