from __future__ import division
import random
import sys


class dice():
    __hiddenvariable = 20
    def dice_roll(self):
        return random.randint(1, 6)

    def number_of_rolls(self):
        return int(input('Enter the number of rolls: '))

    def simulate(self, number_of_times):
        counter = {n : 0 for n in range(2, 13)}
        doubles = 0

        for i in range(number_of_times):
            first_dice = self.dice_roll()
            second_dice = self.dice_roll()
            total = first_dice + second_dice

            doubles += 0 if first_dice != second_dice else 1
            counter[total] += 1

        return counter, doubles

if __name__ == '__main__':
    obj = dice()
    rolls = obj.number_of_rolls()
    counter, doubles = obj.simulate(rolls)  
    total = sum(counter.values())
    # print(obj.__hiddenvariable)
    for total, count in counter.items():
        print("{} - {} {:0.4f}%".format(total, count, count / rolls * 100))

    print("Doubles - {} - {:0.6f}%".format(doubles, doubles / rolls * 100))