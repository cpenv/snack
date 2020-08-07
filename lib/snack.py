# -*- coding: utf-8 -*-
from __future__ import print_function
from random import choice


snacks = [
    'apple',
    'banana',
    'bowl of cereal',
    'some cheese',
    'chocolate chip cookie',
    'chocolate',
    'cracker',
    'grapefruit',
    'ice cream',
    'orange',
    'pretzel',
    'some shortbread',
]


def main():
    snack = choice(snacks)
    article = ('a', 'an')[snack[0] in 'aeiou']
    message = "Here's %s %s!" % (article, snack)
    print(message)


if __name__ == '__main__':
    main()
