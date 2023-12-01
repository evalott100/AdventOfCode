import re

PATTERN = r"\d"

# ===========================================================
# === TERRIBLE SOLUTION BUT I'M EEPY SO IT'LL HAVE TO DO ====
# === ... Actually not too bad - 0.036s for both parts ======
# ===========================================================

# Adding in dummy characters so replacement doesn't interfere
# with other string numbers
STRING_VALUES = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}

file_lines = open(
    "input.txt",
    "r",
).readlines()


def convert_substrings(string):
    for int_str in STRING_VALUES:
        string = re.sub(int_str, STRING_VALUES[int_str], string)
    return string


def first_last_int(string):
    search = re.findall(PATTERN, string)
    tens = search[0]
    # Works even if there's only one digit
    units = search[-1]
    return int(tens + units)


def part_1():
    return sum(first_last_int(line) for line in file_lines)


def part_2():
    return sum(first_last_int(convert_substrings(line)) for line in file_lines)


print(part_1())
print(part_2())