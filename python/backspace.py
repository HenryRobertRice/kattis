string = list(raw_input())
bkspc = 0
for i in range(len(string) - 1, -1, -1):
  if string[i] == "<":
    bkspc += 1
  elif bkspc > 0:
    string[i] = "<"
    bkspc -= 1
print(''.join([c for c in string if c != "<"]))
