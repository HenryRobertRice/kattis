def main():
    while True:
        a, b = map(int, input().split())
        if a == 0 and b == 0:
            return
        a_steps = collatz(a)
        b_steps = collatz(b)
        a_set = set(a_steps)
        for step in b_steps:
            if step in a_set:
                common = step
                break
        a_index = a_steps.index(common)
        b_index = b_steps.index(common)
        print(str(a) + " needs " + str(a_index) + " steps, " + str(b) + " needs " + str(b_index) + " steps, they meet at " + str(int(common)))

def collatz(num):
    steps = []
    while num != 1:
        steps.append(num)
        if num % 2 == 0:
            num /= 2
        else:
            num *= 3
            num += 1
    steps.append(1)
    return steps

if __name__ == "__main__":
    main()
