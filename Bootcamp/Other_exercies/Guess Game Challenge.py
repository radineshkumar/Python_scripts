#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 21:08:26 2018

@author: dineshkumarrajendran
"""

import random
num = random.randint(1,100)
print('---------------------RULES!!!!!--------------------------------')
print('Guess the number between 1 and 100')
print("If your guess number is not between 1 and 100, I will tell you 'OUT OF BOUND'")
print("If your guess number is within 10 of the number, I will tell you 'WARM'")
print("If your guess number is further than 10 away from the number, I will tell you 'COLD'")
print("On subsequent turns, if your guess is closer to the number than the previous guess, I will tell you 'WARMER'")
print("On subsequent turns, if your guess is further away from previous guess, I will tell you 'COLDER'")
print("At the end after your guess is correct, I will tell you how many guesses it took" )
print('---------------------END OF RULES!!!!!--------------------------------')
#print('Randomly picked number:{}'.format(num))

list_guess=[]
guess,prev_guess,count= 0,0,1
    
while (guess!=num):
    guess = int(input('Enter the guess number:'))
    if guess <1 or guess >100:
        print('OUT OF BOUNDS')
    elif (count==1) and (guess in range (num-10, num) or guess in range(num+1,num+11)):
        print('WARM')
    elif (count ==1) and (guess!=num):
        print('COLD')
    elif guess ==num:
        if count ==1:
            print('WOW, CORRECT GUESS IN 1ST ATTEMPT')
            break
        else:
            print('CORRECT GUESS NOW')
    elif guess in range(prev_guess,num) or guess in range (num+1, prev_guess) or guess in range(num-10, num) or guess in range(num, num+11):
        print('WARMER')
    else:
        print('COLDER')
    count+=1
    prev_guess=guess
    list_guess.append(guess)
    
if count>1:
    print('ohhh!! it took {} number of times to guess '.format(len(list_guess)))