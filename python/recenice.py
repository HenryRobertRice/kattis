def main():
    words = [input() for _ in range(int(input()))]
    length = sum([len(w) for w in words if w != "$"])
    for i in range(1, 1000):
        i_string = get_number_string(i)
        if i == length + len(i_string):
            print(get_sentence(i_string, words))
            break


def get_number_string(n):
    n = str(n)
    number_string = ""
    if len(n) == 3:
        number_string += get_hundreds_string(n[0])
        n = n[1:]
    if len(n) == 2:
        number_string += get_tens_string(n)
        if n[0] == "1":
            return number_string
        n = n[1:]
    number_string += get_ones_string(n)
    return number_string


def get_sentence(number_string, words):
    return " ".join([number_string if w == "$" else w for w in words])


def get_hundreds_string(n):
    strings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    return strings[int(n) - 1] + "hundred"


def get_tens_string(n):
    strings = ["", get_teens_string(n), "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    return strings[int(n[0])]


def get_teens_string(n):
    strings = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    return strings[int(n[1])]


def get_ones_string(n):
    strings = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    return strings[int(n)]


if __name__ == "__main__":
    main()
