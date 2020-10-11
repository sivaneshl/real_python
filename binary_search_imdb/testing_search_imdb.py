# Usage:
# py testing_search_imdb.py -a binary "Rajinikanth"

import time
import argparse
from statistics import mean, median
from search.random import find_index as rdn
from search.linear import find_index as lin
from search.binary_iterative import find_index as ibin
from search.binary_recursive import find_index as rbin


def load_names(filename):
    """ load names from file """
    print(f"Loading names...", end="", flush=True)
    with open(filename, encoding='utf-8') as text_file:
        names = text_file.read().splitlines()
        print('ok')
        return names


def parse_args():
    """ parse command line arguments """
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--algorithm', choices=('random', 'linear', 'binary'))
    parser.add_argument('search_term')
    return parser.parse_args()



def convert(nano):
    """ convert nano seconds to a formatted string """
    kilo, mega, giga = 1e3, 1e6, 1e9

    if nano < kilo:
        return f"{nano} ns"
    if nano < mega:
        return f"{nano / kilo:.2f} µs"
    if nano < giga:
        return f"{nano / mega:.2f} ms"
    return f"{nano / giga:.2f} s"


def benchmark(algorithm, elements, value, repeat=10):
    times = []
    for i in range(repeat):
        print(f"[{i+1}/{repeat}] Searching...", end="", flush=True)
        start_time = time.perf_counter_ns()
        index = algorithm(elements, value)
        elapsed_time = time.perf_counter_ns() - start_time
        times.append(elapsed_time)
        print('\b'*12, end="")
        if index is None:
            print(f"Not Found ({convert(elapsed_time)})")
        else:
            print(f"Found at index={index} ({convert(elapsed_time)})")

    print(
        f"best={convert(min(times))}",
        f"worst={convert(max(times))}",
        f"avg={convert(int(mean(times)))}",
        f"median={convert(int(median(times)))}"
    )


def main():
    algorithms = {
        "random": rdn,
        "linear": lin,
        "binary": ibin
    }

    # names = load_names('names.txt')
    names_sorted = load_names('sorted_names.txt')

    args = parse_args()
    benchmark(algorithms[args.algorithm], names_sorted, args.search_term)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('Aborted')

