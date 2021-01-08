from collections import *
import functools
from itertools import *

Info = namedtuple('Info', 'number strike ball')

def is_OK(value):
    global infos
    for info in infos:
        _strike = 0
        _ball = 0
        
        for i in range(3):
            for j in range(3):
                if i == j and info.number[i] == value[j]:
                    _strike += 1
                
                if i != j and info.number[i] == value[j]:
                    _ball += 1

        if info.strike != _strike or info.ball != _ball:
            return False

    return True


n = int(input())

infos = []

for i in range(n):
     number, strike, ball = input().split(' ')
     strike, ball = int(strike), int(ball)
     infos.append(Info(number, strike, ball))

items = tuple('123456789')
count = 0

for i in permutations(items, 3):
    if is_OK(i):
        count += 1

print(count)