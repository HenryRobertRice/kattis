from sys import exit
my_input = input()
if len(my_input.rstrip()) != len(my_input):
    n = int(my_input.rstrip())
    label = 0
    for i in range(n + 1):
        label += 2 ** i
    print(label)
    exit()
else:
    n, seq = my_input.split()
n = int(n)
label = 0
for i in range(n + 1):
    label += 2 ** i
root = label + 1
step = 0
for s in seq:
    if s == 'L':
        label -= (root - label)
    else:
        label -= (root - label + 1)
    step += 1
print(label)
