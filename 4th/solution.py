from time import time_ns


def format_input():
    with open(
        "input.txt",
        "r",
    ) as file:
        input_lines = file.readlines()

    input_data = []
    for line in input_lines:
        line = line.strip().replace("  ", " ")
        choice_string, winning_string = line.strip().split(" | ")
        input_data.append(
            [set(choice_string.split(" ")[2:]), set(winning_string.split(" "))]
        )

    return input_data


INPUT = format_input()
start_time = time_ns()


def number_of_matches(choice_numbers, winning_numbers):
    return len(winning_numbers.intersection(choice_numbers))


MATCHES = [
    number_of_matches(choice_numbers, winning_numbers)
    for choice_numbers, winning_numbers in INPUT
]


def question_1():
    return sum(int(2**matches) for matches in MATCHES)


def question_2():
    number_of_each_card = [1] * len(MATCHES)

    for idx in range(len(number_of_each_card) - 1):
        for i in range(1, MATCHES[idx] + 1):
            number_of_each_card[idx + i] += number_of_each_card[idx]

    return sum(number_of_each_card)


print(question_1())
print(question_2())

time_elapsed = time_ns() - start_time
print(f"{time_elapsed * 10**-6}ms")
