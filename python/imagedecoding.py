from sys import stdin
def print_line(line):
    out_line = []
    char = line[0]
    if char == '.':
        comp_char = '#'
    else:
        comp_char = '.'
    for i in range(1, len(line)):
        if i % 2 == 1:
            out_line.extend(char * int(line[i]))
        else:
            out_line.extend(comp_char * int(line[i]))
    print("".join(out_line))
    return sum([int(x) for x in line[1:len(line)]])

ctr = 0
while True:
    num_lines = int(input())
    if num_lines == 0:
        break
    if ctr != 0:
        print()
    decode_error = False
    lens = set()
    for i in range(num_lines):
        lens.add(print_line(input().split()))
    if len(lens) > 1:
        print("Error decoding image")
    ctr += 1
