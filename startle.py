import random
import argparse
from datetime import datetime
import util.sound as sd
from playsound import playsound
import sys
from time import sleep

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
    parser.add_argument("-w","--wave",type=int, help="db you want to create sound waves")
    parser.add_argument("-d","--duration" ,type=int ,help="duration of sound")
    return parser.parse_args()


def main():
    init_args = init_argparse()
    if init_args.wave and init_args.duration:
        sound = sd.Sound(init_args.wave)
        sound.duration = init_args.duration
        sound.create_sound()
        sys.exit("startle.wav is created")
    if init_args.level and init_args.file:
        trigger_min = generate_random_time(init_args.level)
        all_user_ratings = []
        while True:

            print(trigger_min)
            if int(datetime.now().strftime("%M")) in trigger_min:

                simulate_noise()
                all_user_ratings.append(user_rating())
                print(all_user_ratings)
                sleep(60)

def user_rating():

    rate = input("Scale your startle reflex between 1 and 10.")
    while True:
        if not rate:
            rate = input("Please rate your startle reflex between 1 and 10.")
            continue
        elif 0 <= int(rate) <=10:
            return rate
        else:
           rate = input("Please rate your startle reflex between 1 and 10.")


def simulate_noise(sound_file="startle.wav"):
    playsound("startle.wav")






def generate_random_time(level):

    trigger_min = set()
    if level == 1:
        for i in range(3):
            trigger_min.add(random.randint(1, 59))
    if level == 2:
        for i in range(7):
            trigger_min.add(random.randint(1, 59))

    return trigger_min


main()