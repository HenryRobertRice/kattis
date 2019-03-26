squares = input()
#min size = min power of 2 greater than squares
b = 1
while b < squares:
    b *= 2
out = str(b)
#break squares into powers of 2
chunks = []
while b:
    if squares // b == 1:
        chunks.append(b)
        squares %= b
    b /= 2
b = int(out)
breaks = 0
target = min(chunks)
while(b):
    if b == target:
        break
    b /=2
    breaks += 1
out += " " + str(breaks)
print(out)
