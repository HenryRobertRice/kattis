from sys import exit
ints = [int(x) for x in input().split()]
box = ints[0:6]
h1 = ints[6]
h2 = ints[7]
s1 = []
s2 = []
for i in range(6):
    for j in range(i + 1, 6):
        for k in range(j + 1, 6):
            if box[i] + box[j] + box[k] == h1:
                s1 = [box[i], box[j], box[k]]
                box.remove(box[k])
                box.remove(box[j])
                box.remove(box[i])
                s2 = box
                s1.sort(reverse = True)
                s2.sort(reverse = True)
                for s in s2:
                    s1.append(s)
                print(" ".join([str(x) for x in s1]))
                exit()
