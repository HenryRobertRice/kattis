for i in range(input()):
    act, shift, h, m = raw_input().split()
    shift, h, m = int(shift), int(h), int(m)
    if act == "F":
        m += shift
        h += m // 60
        m %= 60
        h %= 24
    else:
        while m < shift:
            h -= 1
            m += 60
        m -= shift
        if h < 0:
            h += 24
    print(str(h) + " " + str(m))

