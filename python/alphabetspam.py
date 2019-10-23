mystring = input()
denom = len(mystring)
white, lower, upper, symbol = 0, 0, 0, 0
for c in mystring:
    if c == '_':
        white += 1
    elif c.isupper():
        upper += 1
    elif c.islower():
        lower += 1
    else:
        symbol += 1
print(str(white / denom))
print(str(lower / denom))
print(str(upper / denom))
print(str(symbol / denom))
