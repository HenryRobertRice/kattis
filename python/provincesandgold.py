g, s, c = [int(x) for x in raw_input().split()]
total = 3 * g + 2 * s + c
out = ""
if total >= 8:
    out += "Province or "
elif total >= 5:
    out += "Duchy or "
elif total >= 2:
    out += "Estate or "
if total >= 6:
    out += "Gold"
elif total >= 3:
    out += "Silver"
else:
    out += "Copper"
print(out)
