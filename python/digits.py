while True:
    num = input()
    if num == "1":
        print("1")
        continue
    if num == "END":
        break
    seq = [len(num)]
    num = seq[-1]
    while num > 1:
        num = len(str(seq[-1]))
        seq.append(num)
    done = False
    for i in range(1, len(seq)):
        if seq[i] == seq[i - 1]:
            done = True
            print(i)
            break
    if not done:
        print(len(seq) + 1)
