#before input, generate all equations
#generate all possible triples of +,-,*,/
#remember int(x/y)
equations = set()
ops = "+-*/"
oplist = []
for i in range(4):
    for j in range(4):
        for k in range(4):
            tmp = ops[i] + ops[j] + ops[k]
            oplist.append(tmp)
#all possible equations
eqlist = []
eq = ""
for o in oplist:
    eq += "4 " + o[0] + " 4 " + o[1] + " 4 " + o[2] + " 4"
    eq2 = eq.replace("/", "//")
    ans = eval(eq2)
    eq += " = " + str(ans)
    eqlist.append([eq, ans])
    eq = ""
for i in range(int(input())):
    found = False
    ans = int(input())
    for e in eqlist:
        if e[1] == ans:
            print(e[0])
            found = True
            break
    if not found:
        print("no solution")
