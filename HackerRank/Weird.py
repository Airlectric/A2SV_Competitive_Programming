#!/bin/python3

import math
import os
import random
import re
import sys

def weird(n):
    if (n % 2 == 1):
        print('Weird')
    elif (n % 2 == 0) and (2 <= n <= 5):
        print('Weird')
    if (n % 2 == 0) and (n > 20):
        print('Not Weird')


if __name__ == '__main__':
    n = int(input().strip())
    weird(n)
