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
    elif init_args.level and init_args.file:
        trigger_min = generate_random_time(init_args.level)
        all_user_ratings = []
        print("Program launched")
        while True:

            if int(datetime.now().strftime("%M")) in trigger_min:

                simulate_noise()
                all_user_ratings.append(user_rating())
                print('\033[95m' + "Guess when is the next flinch:O" + '\033[0m')


                if init_args.level == 2 and len(all_user_ratings) >= 6:

                    store_file(all_user_ratings,init_args.file)
                    break
                if  init_args.level == 1 and len(all_user_ratings) >= 3:
                    store_file(all_user_ratings,init_args.file)
                    break
                sleep(60)
    else:
        sys.exit("""
        at least two parameters required
        startle.py -l 1 -f history_file -> start training
        startle.py -w 100 -d 5 -> create sound wave
        startle.py --help -> detailed guide
        
        """)

    sys.exit("That's enough training today")

def store_file(list,file):
    sum = 0
    for i in list:
        sum += int(i)
    average = sum/len(list)
    time = datetime.now().strftime("%Y-%m-%d")
    with open(file,"a") as file:
        file.write(f"+{'-' * 10}+{'-' * 10}+{'-' * 10}+\n")
        file.write(f"|{time:^10}|{average:^10}|{len(list):^10}|\n")
        file.write(f"+{'-' * 10}+{'-' * 10}+{'-' * 10}+\n")
        file.write("\n\n\n")
        file.write("/\\" * 33)

def user_rating():

    rate = input("Scale your startle reflex between 1 and 10.\n")
    while True:
        if not rate:
            rate = input("Please rate your startle reflex between 1 and 10.\n")
            continue
        elif 0 <= int(rate) <=10:
            return rate
        else:
           rate = input("Please rate your startle reflex between 1 and 10.\n")


def simulate_noise(sound_file="startle.wav"):
    playsound(sound_file)






def generate_random_time(level):

    trigger_min = set()
    if level == 1:
        while len(trigger_min) <= 3:
            trigger_min.add(random.randint(1, 59))
    if level == 2:
        while len(trigger_min) <= 6:
            trigger_min.add(random.randint(1, 59))

    return trigger_min



if __name__ == "__main__":
    main()