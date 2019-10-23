def main():
    for _ in range(int(input())):
        num = int(input())
        numsum = sumdigits(num)
        for i in range(num - 1, -1, -1):
            if sumdigits(i) == numsum - 1:
                print(i)
                break

def sumdigits(i):
    output = 0
    while i:
        output += i % 10
        i //= 10
    return output

if __name__ == "__main__":
    main()
