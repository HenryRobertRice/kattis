s, c = [int(x) for x in input().split()]
inputs = input().split()
stack = []
for i in range(len(inputs)):
    if inputs[i] == "undo":
        stack.append(inputs[i] + " " + inputs[i + 1])
        i += 1
    elif i > 0 and inputs[i - 1] != "undo":
        stack.append(inputs[i])
    elif i == 0:
        stack.append(inputs[0])
counter = 0
while stack:
    command = stack.pop().split()
    if command[0] == "undo":
        for i in range(int(command[1])):
            stack.pop()
    else:
        counter += int(command[0])
        print("!: " + command[0])
print(str(counter % s))
