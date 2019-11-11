from math import sqrt, floor
from sys import exit

def main():
    word = input()
    #print(floor(sqrt(len(word))))
    for i in range(1, len(word) // 2 + 1):
        if len(word) % i != 0:
            continue
        root = word[0: i]
        rubric = dictify(root)
        isroot = True
        for j in range(len(word) // i - 1):
            #number of remaining strings of len i
            if dictify(word[i + j * i: 2 * i + j * i]) != rubric:
                isroot = False
                break
        if isroot:
            print(word[0: i])
            exit()
    print("-1")

def dictify(string):
    output = dict()
    for s in string:
        if s not in output:
            output[s] = 1
        else:
            output[s] = output[s] + 1
    return output

if __name__ == "__main__":
    main()
