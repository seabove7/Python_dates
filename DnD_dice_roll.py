
import random

dice_string = input('Enter the dice roll: ')

dice_split = dice_string.split('+')

if len(dice_split) > 1:
    roll_modifier = dice_split[1]
    roll_modifier = int(roll_modifier)

dice_type = dice_split[0]
dice_num = dice_type.replace('d', '')
dice_int = int(dice_num)
roll = random.randint(1, dice_int)

if len(dice_split) > 1:
    roll = roll + roll_modifier

print(f'Your awesome roll is: {roll}!')

