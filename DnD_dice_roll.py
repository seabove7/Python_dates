
import random

dice_string = input('Enter the dice roll: ')

roll_list = dice_string.split('d')
dice_split = roll_list[1].split('+')
dice_rep = roll_list[0]


if len(dice_split) > 1:
    roll_modifier = dice_split[1]
    roll_modifier = int(roll_modifier)

dice_type = dice_split[0]
dice_num = dice_type.replace('d', '')
dice_int = int(dice_num)
roll = random.randint(1, dice_int)


if len(dice_split) > 1:
    roll = roll + roll_modifier

print(f'Your awesome roll is: {roll}! (with {num_dice} die/dice)')


