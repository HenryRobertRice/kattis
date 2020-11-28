from sys import stdin


def main():
    defs = dict()
    for line in stdin:
        expr = line.split()
        if expr[0] == "define":
            defs[expr[2]] = int(expr[1])
        else:
            op1 = expr[1]
            op2 = expr[3]
            if op1 not in defs or op2 not in defs:
                print("undefined")
                continue
            if expr[2] == "<":
                print("true" if defs[op1] < defs[op2] else "false")
            elif expr[2] == ">":
                print("true" if defs[op1] > defs[op2] else "false")
            else:
                print("true" if defs[op1] == defs[op2] else "false")


if __name__ == "__main__":
    main()
