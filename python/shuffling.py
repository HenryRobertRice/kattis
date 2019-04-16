from sys import exit
def main():
    n, shuff = input().split()
    cards = [i for i in range(int(n))]
    original = cards
    s = 0
    if shuff == 'in':
        while True:
            cards = in_shuff(cards)
            s += 1
            if cards == original:
                print(str(s))
                break
    else:
        while True:
            cards = out_shuff(cards)
            s += 1
            if cards == original:
                print(str(s))
                break

def out_shuff(cards):
    if len(cards) % 2 == 0:
        mid = len(cards) // 2 - 1
    else:
        mid = len(cards) // 2
    left = cards[0:mid + 1]
    right = cards[mid + 1:]
    output = []
    for i in range(len(right)):
        output.append(left[i])
        output.append(right[i])
    if len(cards) % 2 == 1:
        output.append(left[-1])
    return output

def in_shuff(cards):
    mid = len(cards) // 2 - 1
    left = cards[0:mid + 1]
    right = cards[mid + 1:]
    output = []
    for i in range(len(left)):
        output.append(right[i])
        output.append(left[i])
    if len(cards) % 2 == 1:
        output.append(right[-1])
    return output

if __name__ == "__main__":
    main()
