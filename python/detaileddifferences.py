for i in range(int(input())):
    str1 = input()
    str2 = input()
    str3 = ""
    for j in range(len(str2)):
        if str2[j] == str1[j]:
            str3 += "."
        else:
            str3 += "*"
    print(str1)
    print(str2)
    print(str3)
    print()
