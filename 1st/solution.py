# ===========================================================
# === TERRIBLE SOLUTION BUT I'M EEPY SO IT'LL HAVE TO DO ====
# === ...Actually not too bad: 7ms for both parts together ==
# ===========================================================

from time import time_ns
import re

start_time = time_ns()

# Adding in dummy characters so replacement doesn't interfere
# with other string numbers:
# "nineighthree" should go to "983" not "9igh3"

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
    search = re.findall(r"\d", string)
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

time_elapsed = time_ns() - start_time
print(f"{time_elapsed * 10**-6}ms")