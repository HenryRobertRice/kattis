from sys import stdin

votes = dict()
while True:
    temp = stdin.readline().rstrip()
    if temp == "***":
        break
    if temp not in votes:
        votes[temp] = 1
    else:
        votes[temp] = votes[temp] + 1
max_ = 0
candidate = ""
for vote in votes:
    if votes[vote] > max_:
        max_ = votes[vote]
        candidate = vote

num = 0

for vote in votes:
    if votes[vote] == max_:
        num += 1

if num > 1:
    print("Runoff!")
else:
    print(candidate)
