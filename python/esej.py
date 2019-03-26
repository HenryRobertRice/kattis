chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
def genword(i):
    out = ""
    while i:
        out += chars[i % 10]
        i //= 10
    return out
a, b = [int(x) for x in input().split()]
#generate b distinct words with length 1 to 15
essay = []
for i in range(1, b + 1):
    essay.append(genword(i))
print(" ".join(essay))
