from sys import stdin
while True:
    jack, jill = map(int, input().split())
    if jack == 0 and jill == 0:
        break
    output = 0
    jack_set = set(int(stdin.readline()) for _ in range(jack))
    jill_set = set(int(stdin.readline()) for _ in range(jill))
    print(len(jack_set.intersection(jill_set)))
