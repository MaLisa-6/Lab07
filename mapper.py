#!/usr/bin/env python3

import sys

def mapper():
    for line in sys.stdin:
        if len(line.strip().split(",")) == 4:
            data = line.strip().split(",")
            timestamp, city, item, cost = data
            print(city + "," + cost)
        elif len(line.strip().split(",")) > 4:
            data = line.strip().split(",")[0:4]
            timestamp, city, item, cost = data
            print(city + "," + cost)
        else:
            pass

if __name__ == "__main__":
    # what function should run when python mapper.py is called?
    mapper()
