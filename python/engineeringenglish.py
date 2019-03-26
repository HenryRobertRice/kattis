from sys import stdin
words = []
for line in stdin:
    output = ""
    for word in line.split():
        temp = word.lower()
        if temp not in words:
            words.append(temp)
            output += word + " "
        else:
            output += ". "
    print(output[:-1])
