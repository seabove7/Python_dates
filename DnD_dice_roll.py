
import random

dice_string = input('Enter the dice roll: ')

roll_list = dice_string.split('d')
dice_split = roll_list[1].split('+')
dice_rep = roll_list[0]
dice_rep = int(dice_rep)


if len(dice_split) > 1:
    roll_modifier = dice_split[1]
    roll_modifier = int(roll_modifier)

dice_type = dice_split[0]
dice_num = dice_type.replace('d', '')
dice_int = int(dice_num)

roll_total = 0

natural = False

for i in range(dice_rep):
    roll = random.randint(1, dice_int)
    if dice_type == '20' and roll == 20:
        natural = True

    roll_total += roll

if len(dice_split) > 1:
    roll_total = roll_total + roll_modifier

dice = 'die'

if dice_rep > 1:
    dice = 'dice'

print(f'{"OMG, you got a nat 20!" if natural else ""} Your awesome roll is {roll_total} (with {dice_rep} {dice})! Nicely done friend.')
