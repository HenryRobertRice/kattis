for i in range(int(input())):
    num = int(input())
    if str(num) == str(num)[::-1]:
        print(str(num))
    else:
        #find lower
        pl = -1
        for i in range(num - 1, 100000, -1):
            if str(i) == str(i)[::-1]:
                pl = i
                break;
        #find higher
        ph = -1
        for i in range(num + 1, 1000000):
            if str(i) == str(i)[::-1]:
                ph = i
                break;
        if pl == -1 or abs(num - ph) < abs(num - pl):
            print(str(ph))
        elif ph == -1 or abs(num - pl) <= abs(num - ph):
            print(str(pl))
