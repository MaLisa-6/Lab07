#!/usr/bin/env python3

import sys

def reducer():
    city_max = 0
    oldKey = None

    for line in sys.stdin:
        data = line.strip().split(",")

        thisKey, thisCost = data
        if oldKey is not None and oldKey != thisKey:
            print(oldKey + "," + str(city_max))
            city_max = 0

        oldKey = thisKey
        if float(thisCost) > float(city_max):
            city_max = thisCost

    if oldKey is not None: # for the final key
        print (oldKey + "," + str(city_max))

if __name__ == "__main__":
    # what function should run when python reducer.py is called?
    reducer()
