'''Happy Birthday in Python Code
- The Original One'''
import time
from random import randint

for i in range(1,85):
    print('')
 
space = ''
for i in range(1,1000):
    count = randint(1, 100)
    while(count > 0):
        space += ' '
        count -= 1
    if(i%10==0):
        print(space + 'ðHappy Birthday To Pisey!')
    elif(i%9 == 0):
        print(space + "ð")
    elif(i%5==0):
        print(space +"ð")
    elif(i%8==0):
        print(space + "ð")
    elif(i%7==0):
        print(space + "ð«")
    elif(i%6==0):
        print(space + "Happy Birthday To Pisey!ð")
    else:
        print(space + "ð¸")
    space = ''
    time.sleep(0.2)