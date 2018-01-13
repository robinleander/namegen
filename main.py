#!/usr/bin/env python3

import random
import argparse

class Source:
    def __init__(self, fname):
        self.list = None
        self.fname = fname

    def random_choice(self):
        if self.list is None:
            with open(self.fname, 'r') as f:
                self.list = list(filter(lambda x: len(x) > 0, f.read().split('\n')))
        return random.choice(self.list)

def genName(sources):
    name = ''
    for source in sources:
        name += random.choice(source).random_choice().capitalize()
    return name

def main():
    ATTRIBS = 'adjectives.txt'
    ANIMALS = 'animals.txt'
    FRUITS = 'fruits.txt'
    sources = [
            [Source(fname) for fname in sourcelist]
            for sourcelist in [[ATTRIBS], [ANIMALS, FRUITS]]
        ]
    parser = argparse.ArgumentParser()
    parser.add_argument("count", help="number of names to generate")
    args = parser.parse_args()
    for _ in range(10 if args.count is None else int(args.count)):
        print(genName(sources))


if __name__ == '__main__':
    main()
