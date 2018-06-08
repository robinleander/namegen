#!/usr/bin/env python3

import random
import argparse
import requests

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


def twitter_check(name):
    return requests.get('https://twitter.com/' + name).status_code == 404


def lol_check(name):
    return 'is available' in requests.get('https://lolnames.gg/en/euw/' + name).text


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
        name = genName(sources)
        if all(f(name) for f in [twitter_check, lol_check]):
            print("\033[1;32m{}\033[0m".format(name))
        else:
            print("\033[1;31m{}\033[0m".format(name), end='')


if __name__ == '__main__':
    main()
