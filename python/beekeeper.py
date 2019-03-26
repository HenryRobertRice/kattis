def score(w):
    score = 0
    for i in range(len(w) - 1):
        if w[i] == w[i + 1] and w[i] in ["a", "e", "i", "o", "u", "y"]:
            score += 1
    return score
while True:
    words = []
    i = int(input())
    if i == 0:
        break
    for j in range(i):
        words.append(input())
    print(max(words, key = lambda word: score(word)))
