def main():
    while True:
        n = int(input())
        if n == 0:
            break
        msg = input().replace(" ", "").upper()
        if n > len(msg):
            print(msg)
        else:
            print(encrypt(n, msg))

def encrypt(n, msg):
    out = list(msg)
    index = 0
    for i in range(len(msg)):
        if index == len(msg):
            break
        for j in range(i, len(msg), n):
            out[j] = msg[index]
            index += 1
    return "".join(out)

if __name__ == "__main__":
    main()
