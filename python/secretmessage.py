#read
#find matrix side length
#fill matrix
#read matrix into output
#print output
for i in range(int(input())):
    message = input()
    msl = 0
    for i in range(1, 1000):
        if i ** 2 >= len(message):
            msl = i
            break
    mat = [["*" for i in range(msl)] for j in range(msl)]
    n = 0
    for i in range(msl):
        for j in range(msl):
            mat[i][j] = message[n]
            n += 1
            if n >= len(message):
                break
        else:
            continue
        break
    output = ""
    for i in range(msl):
        for j in range(msl - 1, -1, -1):
            output += mat[j][i]
    output = "".join([c for c in output if c != "*"])
    print(output)
