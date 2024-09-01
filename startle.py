import random
import argparse
from datetime import datetime


def init_argparse():
    parser = argparse.ArgumentParser(
        prog="startle", description="Startle measurement application", epilog="to do"
    )
    parser.add_argument(
        "-l",
        "--level",
        choices=range(1, 3),
        default=1,
        type=int,
        help="Set the noise level",
    )
    parser.add_argument("-f", "--file", type=str, help="File to store results")
    return parser.parse_args()


def main():


    print(generate_random_time(2))


def generate_random_time(level):
    duration = []
    trigger_min = set()
    if level == 1:
        for i in range(3):
            duration.append(random.randint(2, 5))
            trigger_min.add(random.randint(int(datetime.now().strftime("%M")), 59))
    if level == 2:
        for i in range(7):
            duration.append(random.randint(3, 7))
            trigger_min.add(random.randint(int(datetime.now().strftime("%M")), 59))

    return duration, trigger_min


main()
