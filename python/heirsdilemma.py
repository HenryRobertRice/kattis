def isValid(n):
    temp = n
    digits = []
    while temp:
        digits.append(temp % 10)
        temp //= 10
    for digit in digits:
        if digit == 0:
            return False
        if digits.count(digit) > 1 or n % digit != 0 or digit == 0:
            return False
    return True;
total = 0
low, high = [int(x) for x in input().split()]
for i in range(low, high + 1):
    if isValid(i):
        total += 1
print(total)
