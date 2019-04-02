#### Python Dice Roller ####

### Import
import random

### Function
# Begins the welcome screen
def welcome():
    print()
    print('''______        _    _                    ______  _             ''')
    print('''| ___ \      | |  | |                   |  _  \(_)            ''')
    print('''| |_/ /_   _ | |_ | |__    ___   _ __   | | | | _   ___  ___  ''')
    print('''|  __/| | | || __|| '_ \  / _ \ | '_ \  | | | || | / __|/ _ \ ''')
    print('''| |   | |_| || |_ | | | || (_) || | | | | |/ / | || (__|  __/ ''')
    print('''\_|    \__, | \__||_| |_| \___/ |_| |_| |___/  |_| \___|\___| ''')
    print('''        __/ |                                                 ''')
    print('''       |___/                                                  ''')

    print()
    print('         ~ Enter your dice roll in xdy format ~')
    print()

# User input parsed into a list, finds the list length, and where the 'd' is located
def input_parse():
    # Takes user input and converts to a list
    roll_list = list(input('What are you rolling?: '))
    # Finds where the 'd' is
    d_pos = roll_list.index('d')
    # Finds how long the list is
    len_list = len(roll_list)
    return d_pos, roll_list, len_list

# Finds number of dice
def dice_no(d_pos, roll_list):
    result = ''
    read_from = 0
   # Loop to keep on reading the list for how many dice there are
    while read_from < d_pos:
        result += roll_list[read_from]
        read_from += 1
    return int(result)

# Finds the number of sides the dice has
def dice_chance(d_pos, roll_list, len_list):
    result = ''
    read_from = d_pos + 1
    # loop to keep on reading the list for how many sides the die has
    while read_from < len_list:
        result += roll_list[read_from]
        read_from += 1
    return int(result)

# Finds the random roll of a specified dice
def roll_die(dice_chance):
    die_value = random.randint(1, dice_chance)
    return die_value

# Rolls the amount of dice required
def full_roll(dice_no, dice_chance):
    reps = dice_no
    sum_total = 0
    dice_list = []
    while reps > 0:
        sum_total += roll_die(dice_chance)
        dice_list.append(roll_die(dice_chance))
        reps -= 1
    return sum_total, dice_list

# Lists off the count for every possibility
def print_dice_list(dice_list, d_pos, roll_list, len_list):
    column_size = dice_chance(d_pos, roll_list, len_list)
    tally = 1
    while tally <= column_size:
        print(str(tally) + 's: ' + str(dice_list.count(tally)))
        tally += 1

# Run order
def program():
    welcome()
    while True:
        try:
            # Create the variables from their respective functions
            d_pos, roll_list, len_list = input_parse()
            sum_total, dice_list = full_roll(dice_no(d_pos, roll_list), dice_chance(d_pos, roll_list, len_list))
            # Human readable output
            print('You rolled: ' + str(sum_total))
            print()
            print('Dice list: ')
            print_dice_list(dice_list, d_pos, roll_list, len_list)
            print()
        #Error checking
        except ValueError:
            print('Must contain a valid xdy format dice roll')
            print('')

# Program Trigger
program()