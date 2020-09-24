from math import ceil

def main():
    action_times = dict()
    for _ in range(int(input())):
        d, t = map(int, input().split())
        update_times(action_times, d, t)
    print(ceil(max(action_times.values()) / 2))


def update_times(a, d, t):
    for i in [t, t - d, t - 2 * d]:
        if i not in a:
            a[i] = 1
        else:
            a[i] += 1


if __name__ == "__main__":
    main()
