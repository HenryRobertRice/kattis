from sys import stdin
def translate(num, d1, d2, d3):
    temp = d3.get(num)
    if temp:
        return temp
    temp = d2.get(num)
    if temp:
        return temp
    return d1.get(num // 10) + "-" + d2.get(num % 10)
d2 = {0: "", 1: "one", 2: "two", 3: "three", 4: "four",
      5 :"five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
d1 = {2: "twenty", 3: "thirty", 4: "forty", 5 :"fifty", 
      6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}
d3 = {10 :"ten", 11: "eleven", 12: "twelve", 13: "thirteen",
      14: "fourteen", 15: "fifteen", 16 :"sixteen", 17: "seventeen",
      18: "eighteen", 19: "nineteen", 0: "zero", 20: "twenty",
      30: "thirty", 40: "forty", 50: "fifty", 60: "sixty",
      70: "seventy", 80: "eighty", 90: "ninety"}
for line in stdin:
    output = ""
    for word in line.split():
        if word.isnumeric():
            output += translate(int(word), d1, d2, d3) + " "
        else:
            output += word + " "
    output = output.capitalize()
    print(output[:-1])
