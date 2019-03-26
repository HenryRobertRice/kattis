from sys import stdin
from string import digits
case = 0
for line in stdin:
    case += 1
    expr = line.split()
    #read right to left
    #when an operator is found, check if there are 2 numbers to the right
    #if so, replace the operator with the result and keep going
    #replace any modified numbers/operators with "?"
    #at end, join all non-"?" with spaces and print
    for i in range(len(expr) - 1, -1, -1):
        if expr[i] in ["+", "-", "*"]:
            if expr[i + 1][-1] in digits and expr[i + 2][-1] in digits:
                if expr[i] == "+":
                    expr[i] = str(int(expr.pop(i + 1)) + int(expr.pop(i + 1)))
                elif expr[i] == "-":
                    expr[i] = str(int(expr.pop(i + 1)) - int(expr.pop(i + 1)))
                elif expr[i] == "*":
                    expr[i] = str(int(expr.pop(i + 1)) * int(expr.pop(i + 1)))
    print("Case " + str(case) + ": " + " ".join([x for x in expr if x != "?"]))
