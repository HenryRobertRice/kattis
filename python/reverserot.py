import sys
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
  line = raw_input()
  if line[0] == "0":
    sys.exit()
  rot, message = line.split()
  message = message[::-1]
  output = ""
  for char in message:
    index = alphabet.find(char) + int(rot)
    if index > 27:
      index -= 28
    output += alphabet[index]
  print output
