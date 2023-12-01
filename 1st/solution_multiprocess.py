# ===========================================================
# === TERRIBLE SOLUTION BUT I'M EEPY SO IT'LL HAVE TO DO ====
# === Decided to write multiprocessing since I'm bored. =====
# === With so little data it's obviously slower in this =====
# === case. A lot faster if the data is 1000 times larger ===
# === than the question though! =============================
# ===========================================================

from time import time_ns
import re
from multiprocessing import Process, cpu_count, Queue

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


total_file_lines = open(
    "input.txt",
    "r",
).readlines() * 1000

def run_part_multiprocessing(part):
    output_queue = Queue()

    processes = []

    slice_size = int(len(total_file_lines) / cpu_count())
    slices = [[process * slice_size , (process + 1) * slice_size] for process in range(cpu_count())]
    slices[-1][1] = len(total_file_lines)

    for process, slice in zip(range(cpu_count()), slices):
        process = Process(target=part, args=(total_file_lines[slice[0]:slice[1]], output_queue, process))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    return sum(output_queue.get_nowait() for _ in range(output_queue.qsize()))



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


def part_1(file_lines, queue, rank):
    print(f"rank {rank} starting part 1")
    queue.put_nowait(sum(first_last_int(line) for line in file_lines))
    print(f"rank {rank} finished part 1")


def part_2(file_lines, queue, rank):
    print(f"rank {rank} starting part 2")
    queue.put_nowait(sum(first_last_int(convert_substrings(line)) for line in file_lines))
    print(f"rank {rank} finished part 2")


print(run_part_multiprocessing(part_1))
print(run_part_multiprocessing(part_2))
time_elapsed = time_ns() - start_time
print(f"{time_elapsed * 10**-6}ms")
