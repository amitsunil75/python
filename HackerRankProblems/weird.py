import math
import os
import random
import re
import sys

n = input('enter a number:').strip()
if __name__ == '__main__':
 if n.isnumeric():
    d=int(n)
    if(d%2==0):
        if(d >=2 and d<6):
            print('NotWeird')
        elif(d<=20 ):
            print('Weird')
        elif(d>20):
            print('NotWeird')
    else:
        print('Weird')
 else:
    print('invalid input')