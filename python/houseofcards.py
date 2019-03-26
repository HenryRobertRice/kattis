def numcards(h):
    return h * (h + 1) // 2 * 3 - h
minheight = int(input())
while True:
    if numcards(minheight) % 4 == 0:
        print(minheight)
        break
    minheight += 1
