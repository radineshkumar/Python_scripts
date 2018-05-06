#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 06:56:19 2018

@author: dineshkumarrajendran
"""

import random

#------------------------------------------------------------------------------

def player_input():
    while True:
        player1 = input("Player1: Do you want to be 'X' or 'O'?\n")
        if player1.lower()=='x' or player1.upper()=='X':
            return 'X'
            break
        elif player1.lower()=='o' or player1.upper()=='O':
            return 'O'
            break
        else:
            print("\033[1;31;47m INVALID, valid response: 'X' or 'O'.....\033[0;0m")
            continue

#------------------------------------------------------------------------------
def display_board(board):
    print("       |       |        ")
    print("   {}   |   {}   |   {}     ".format(board[0], board[1], board[2]))
    print("       |       |        ")
    print("-----------------------")
    print("       |       |        ")
    print("   {}   |   {}   |   {}     ".format(board[3], board[4], board[5]))
    print("       |       |        ")
    print("-----------------------")
    print("       |       |        ")
    print("   {}   |   {}   |   {}     ".format(board[6], board[7], board[8]))
    print("       |       |        ")

#------------------------------------------------------------------------------
def place_marker(board, marker, position):
    if position not in range(1,10):
        return False
    for index, item in enumerate(board):
        if index+1 == position:
            if board[index]==' ':
                board[index]=marker
            else:
                print('\033[1;31;47m The position {} is already occupied in the board, choose different position \033[0;0m'.format(position))
                return False
    #    win_check(board, marker, position)
    return True
#------------------------------------------------------------------------------

def win_check(board,marker):
        if (board[0]==marker and board[1]==marker and board[2]==marker) or (board[0]==marker and board[3]==marker and board[6]==marker) or (board[0]==marker and board[4]==marker and board[8]==marker) or (board[1]==marker and board[4]==marker and board[7]==marker) or (board[6]==marker and board[7]==marker and board[8]==marker) or (board[2]==marker and board[5]==marker and board[8]==marker) or (board[2]==marker and board[4]==marker and board[6]==marker) or (board[3]==marker and board[4]==marker and board[5]==marker):
            return True
        else:
            return False
#------------------------------------------------------------------------------      

def random_player():
    return str(random.randint(1,2))

#------------------------------------------------------------------------------
    
def replay():
    while True:
        replay = input('Do you want to replay the game? Yes/No\n')
        if replay.upper()=='YES':
            return True
            break
        elif replay.upper()=='NO':
            return False
            break
        else:
            print('\033[1;31;47m INVALID, valid response: Yes or No \033[0;0m')
            continue
 
#------------------------------------------------------------------------------       
        
print('"\033[1;31;47m ********* Welcome to Tic Tac game ********* \033[0;0m')

while True:
    game_play = input('Are you ready to play the game? Please enter Yes/No\n')
    if not(game_play.lower()=='no' or game_play.lower()=='yes'or game_play.lower()=='n'or game_play.lower()=='y'):
        print('\033[1;31;47m INVALID, valid response: Yes or No \033[0;0m')
        print('\n'*20)
        continue
    if game_play.lower()=='no' or game_play.lower()=='n' :
        print('OK, no problem.. Come back later to play the game')
        break
    player1_marker = player_input()
    if player1_marker == 'X':
        #print('Player1 will go first')
        player2_marker= 'O'
    else:
        player2_marker = 'X'
    randompick = random_player()
    if  randompick == '1':
        player1 = 'player1'
        player2 = 'Player2'
        marker1 = player1_marker
        marker2 = player2_marker
        print("Player1 will go first based on random pick")
    else:
        player1 = 'Player2'
        player2 = 'Player1'
        marker1 = player2_marker
        marker2=  player1_marker
        print("Player2 will go first based on random pick")
    while True:
        start = input('Shall we start the game? Please enter Yes/No \n')
        if not(start.lower()=='yes' or start.lower()=='y' or start.lower()=='no' or start.lower()=='n'):
            print("\033[1;31;47m INVALID, valid response: Yes/No \033[0;0m")
            continue
        else:
            break
    if start.lower() == 'no' or start.lower()=='n':
        print('OK, see you later..')
        print('\n'*20)
        break
    print('\n'*20)
    test_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    display_board(test_board)
    while True:
        while True:
            player1_position = input(player1+ ': Please choose your next position (1 to 9)\n')
            if player1_position not in ['1','2','3','4','5','6','7','8','9']:
                print('\033[1;31;47m  Invalid position\n \033[0;0m')
                continue
            else:
                player1_position=int(player1_position)
            player1_result = place_marker(test_board, marker1, player1_position)
            if player1_result ==False:
                continue
            else:
                result = win_check(test_board, marker1)
                print('\n'*20)
                display_board(test_board)
                break
        if result == True:
            print("\033[1;31;47m YOU WON!!!!!! CONGRATULATIONS \033[0;0m")
            break
        if " " not in test_board:
            print("\033[1;31;47m  IT'S A TIE!!!!!!  \033[0;0m")
            break        
        while True:
            player2_position = input(player2+': Please choose your next position (1 to 9)\n')
            if player2_position not in ['1','2','3','4','5','6','7','8','9']:
                print('\033[1;31;47m  Invalid position\n \033[0;0m')
                continue
            else:
                player2_position=int(player2_position)
            player2_result = place_marker(test_board,marker2, player2_position)
            if player2_result ==False:
                continue
            else:
                result = win_check(test_board, marker2)
                print('\n'*20)
                display_board(test_board)
                break
        if result == True:
            print("\033[1;31;47m YOU WON!!!!!! CONGRATULATIONS \033[0;0m")
            break
    if not replay():
            break;


    
