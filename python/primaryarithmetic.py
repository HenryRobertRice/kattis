from sys import exit
def main():
    while True:
        n1, n2 = input().split()
        if (n1, n2) == ("0", "0"):
            exit()
        count_operations(n1, n2)

def count_operations(n1, n2):
    n1 = n1[::-1]
    n2 = n2[::-1]
    num_carry = 0
    carry = 0
    for i in range(0, min(len(n1), len(n2))):
        if int(n1[i]) + int(n2[i]) + carry > 9:
            carry = 1
            num_carry += 1
        else:
            carry = 0
    if carry == 1:
        if len(n1) > len(n2):
            num_carry += ripple(n1, len(n2))
        if len(n2) > len(n1):
            num_carry += ripple(n2, len(n1))
    output = ""
    if num_carry == 0:
        output += "No"
    else:
        output += str(num_carry)
    output += " carry operation"
    if num_carry > 1:
        output += "s"
    output += "."
    print(output)

def ripple(n, l):
    output = 0
    for i in range(l, len(n)):
        if n[i] == "9":
            output += 1
        else:
            return output
    return output

if __name__ == "__main__":
    main()
