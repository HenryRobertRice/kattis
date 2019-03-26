from sys import exit
string = raw_input()
for i in range(0, len(string) - 1):
    if string[i] == "s" and string[i + 1] == "s":
        print("hiss")
        exit()
print("no hiss")
