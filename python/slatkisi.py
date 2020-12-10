def main():
    c, k = map(int, input().split())
    k = 10 ** k
    round_down = c // k * k
    round_up = round_down + k
    print(round_down if abs(round_down - c) < abs(round_up - c) else round_up)


if __name__ == "__main__":
    main()
