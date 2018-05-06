#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 05:31:55 2018

@author: dineshkumarrajendran
"""
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}

chips_total_value = 0
hit_value = 21


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        c_str = self.rank + ' of ' + self.suit
        self.display_card(c_str)
#        return (f'\t {self.rank} of {self.suit}')
        return ""

    def display_card(self, card_info):
        print("    --------------------")
        print("    |                  |")
        print("    |                  |")
        print("    | {}".format(card_info))
        print("    |                  |")
        print("    |                  |")
        print("    -------------------- ")


class Deck:

    def __init__(self):
        self.deck = []
        rank_list = []
        for suit in suits:
            for rank in ranks:
                rank_list.append(suit)
                rank_list.append(rank)
                self.deck.append(rank_list)
                rank_list = []

    def shuffle(self):
        random.shuffle(self.deck)

    def random(self):
        return random.choices(self.deck)
    
    def remove(self, card):
        random_pick_index = self.deck.index(card[0])
        self.deck.pop(random_pick_index)

    def pick_card(self):   
        return self.deck.pop(0)
    
    def display_deck(self):
        print(self.deck)
        

class Chips:
    
    def __init__(self, balance):
        self.balance = balance

    def chips_balance(self):
        return self.balance
        
    def chips_balance_check(self, amount):
        if self.balance > amount:
            return True
        else:
            return False
        
    def win_bet(self, won_amount):
        self.balance = self.balance + won_amount
        
    def lose_bet(self, lost_amout):
        self.balance = self.balance - lost_amout

    def __str__(self):
        return 'The chips balance : $' + str(self.balance)


class Hand:

    global hit_value

    def __init__(self, total_card_value, ace_adj=0):
        self.total_card_value = total_card_value
        if ace_adj != 0:
            self.ace_adjustment()

    def is_bust(self):
        if self.total_card_value > hit_value:
            return True
        else:
            return False

    def is_hit(self):
        if self.total_card_value == hit_value:
            return True
        return False

    def ace_adjustment(self):
        if self.total_card_value > hit_value:
            self.total_card_value = self.total_card_value-10

    def __str__(self):
        return str(self.total_card_value)


# get rank value
def get_rank_value(suit_rank):
    for key, value in values.items():
        if suit_rank[1] == key:
            return value

    return -1


# purchase chips
def purchase_chips():
    global chips_total_value

    if chips_total_value == 0:
        print("Hello Player, please purchase the chips to play the game \n")
    else:
        while True:
            buy_chips = input('Do you want to purchase chips now? - Please enter Yes/No...\n')
            if buy_chips.lower() == 'no':
                return -1
            elif buy_chips.lower() == 'yes':
                break
            else:
                print("\033[1;31;47m Invalid input. Please retry.....\033[0;0m")
                continue

    while True:
        try:
          # Get input from player
            chips_value = float(input('What is the total $ chips value you would like to purchase? \n'))
            chips_total_value = chips_total_value + chips_value
            break
        except:
            print("\033[1;31;47m Invalid input. Please retry.....\033[0;0m")
            continue

    # display total chips value
    print("Your total chips balance: $"+str(chips_total_value))


# Game ready to play?
def ready_to_play():

    while True:
        game_start = input('Are you ready to play the game? Please enter Yes/No \n')
        if game_start.lower() == 'yes':
            return True
        elif game_start.lower() == 'no':
            return False
        else:
            print("\033[1;31;47m Invalid input. Please retry.....\033[0;0m")
            continue


# play again?
def play_again():

    while True:

        try:
            game_start = input('Do you want to play again? Please enter Yes/No \n')
            if game_start.lower() == 'yes':
                return True
            elif game_start.lower() == 'no':
                return False
            else:
                print("\033[1;31;47m Invalid input. Please retry.....\033[0;0m")
                continue
        except:
            print("\033[1;31;47m Invalid input. Please retry.....\033[0;0m")
            continue


# player option
def player_option(cBalance):

    print('Sorry, no sufficient chips to play the game. Either purchase the additional chips or reduce bet amount')
    while True:
        usr_input = input("Do you want to purchase chips or reduce bet value or exit the game? ..." \
                          "Enter short keyword answer - Chips/Bet/Exit...\n")
        if usr_input.lower() == 'exit':
            return 0
        elif usr_input.lower() == 'chips':
            return 1
        elif usr_input.lower() == 'bet':
            while True:
                    try:
                        reduce_bet = int(input("Enter the reduced bet value..."))
                        if reduce_bet > cBalance:
                            print("Reduced Bet value is greater than chips balance - {}. Please try again".format(cBalance))
                            continue
                        else:
                            return reduce_bet
                    except:
                        print("\033[1;31;47m Invalid input. Please retry.....\033[0;0m")
                        continue
        else:
            print("\033[1;31;47m Invalid input. Please retry.....\033[0;0m")
            continue


# check if deal wins
def dealer_wins(dealer_value, player_value):
    if (dealer_value > player_value) and (dealer_value <= hit_value):
        return True
    return False


# dealer ace adjustment
def dealer_ace_adj(dealer_value):
    if dealer_value > hit_value:
        return dealer_value - 10
    return dealer_value


# Game banner display
print('\n\033[;1m ********Welcome to BlackJack Game******** \033[0;0m \n')
print('############### RULES OF GAME ############### ')
print('2 people involved in the game - DEALER AND PLAYER \n'
      'Dealer and player pick 2 card each from the shuffled deck \n'
      "Display only one of the Dealer's cards, the other remains hidden \n"
      "Display both player's card \n"
      'Player has option to Hit or Stand if player cards does not hit card value 21\n'
      'If player choose to Hit, then another card will be taken from the deck\n'
      'If player choose to stand then dealer turn to play\n'
      "The dealer will always Hit until the player's value meets or exceeds 21")
print('################################################')

while True:
    # call the method to purchase the chips
    purchase_chips()
    c = Chips(chips_total_value)
    # get the bet value from the player
    bet_value = float(input('What is your bet amount?\n'))
    # check bet value is less than chips balance
    if c.chips_balance_check(bet_value) is True:
        print('Congratulation, you have sufficient chips to play the game')
    else:
        option = player_option(c.chips_balance())
        if option == 0:
            break
        elif option == 1:
            continue
        else:
            bet_value = option
    # ready to start the game?
    if ready_to_play() == False:
        break
    # create an object for Deck() class and call shuffle method
    deck = Deck()
    deck.shuffle()
    # pick 2 cards for player and dealer
    print('picking 2 cards for Player')
    player_list = []
    player_card1 = deck.pick_card()
    player_list.append(player_card1)
    player_card2 = deck.pick_card()
    player_list.append(player_card2)
    dealer_card1 = deck.pick_card()
    dealer_card2 = deck.pick_card()
    print(player_list)
    print('***********************')
    print("The player's open cards are")
    player_total = 0
    dealer_total = 0
    ace_enter = ""
    for value in range(len(player_list)):
        print(Card(player_list[value][0], player_list[value][1]))
        player_total = player_total + get_rank_value(player_list[value])
        if player_list == 'Ace':
            ace_enter = 1
    # create a object for player with cards
    player_hand = Hand(player_total, ace_enter)
    print('Player total card value :' + player_hand.__str__())

    # check the player wins
    if player_hand.is_hit():
        c.win_bet(bet_value)
        print('Congratulation!!! you hit the blackjack')
        print('Your chips balance now : ' + str(c.balance))
        chips_total_value = c.balance
        if play_again():
            continue
        else:
            break
    if player_hand.is_bust():
        c.lose_bet(bet_value)
        print('Bust - you lost the game!!!')
        print('Your chips balance now : ' + str(c.balance))
        chips_total_value = c.balance
        if play_again():
            continue
        else:
            break
    print('***********************')
    print('The dealer open card is')
    print(Card(dealer_card1[0], dealer_card1[1]))
    dealer_total = dealer_total+get_rank_value(dealer_card1)
    print('Dealer open card value : ' + str(dealer_total))
    print('***********************')

    while True:
        Flag = 0
        ace_enter = 0
        while True:
            player_choice = input('Dealer to Player: Hit or Stand?\n')
            if player_choice.lower() == 'hit' or player_choice.lower() == 'stand':
                break
            else:
                print("\033[1;31;47m Invalid input. Please retry.....\033[0;0m")
                continue

        if player_choice.lower() == 'hit':
            player_card = deck.pick_card()
            print(Card(player_card[0], player_card[1]))
            player_hand.total_card_value = player_total+get_rank_value(player_card)
            if player_card == 'Ace':
                player_hand.ace_adjustment()
            player_total = player_hand.total_card_value
            print('Player total card value : ' + str(player_total))
            # check the player wins
            if player_hand.is_hit():
                c.win_bet(bet_value)
                print('\033[1;31;47m ################ GAME RESULT ########################\033[0;0m')
                print('Congratulation!!! you hit the blackjack')
                # print('########################################')
                Flag = 1
                break
            elif player_hand.is_bust():
                c.lose_bet(bet_value)
                print('\033[1;31;47m ################ GAME RESULT ########################\033[0;0m')
                print('Bust - you lost the game!!!')
                # print('########################################')
                Flag = 1
                break
            else:
                continue
        else:
            break

    print('Your chips balance now: ' + str(c.balance))
    chips_total_value = c.balance
    if Flag == 1:
        if play_again():
            continue

    # now dealer's turn to open the 2nd card
    print('***********************')
    print('Dealer opens up 2nd card')
    print(Card(dealer_card2[0], dealer_card2[1]))
    dealer_total = dealer_total+get_rank_value(dealer_card2)
    print("Dealer's 2nd card value : " + str(dealer_total))
    print('***********************')
    while True:

        # dealer ace card present check
        if dealer_card1 == 'Ace' or dealer_card2 == 'Ace':
            dealer_total = dealer_ace_adj(dealer_total)

        print('Dealer total card value : ' + str(dealer_total))

        # check if dealer card value exceeds hit value
        if dealer_total > hit_value:
            print('\033[1;31;47m ################ GAME RESULT ########################\033[0;0m')
            print('Dealer Bust -  lost the game!!!')
            c.win_bet(bet_value)
            break
        # check dealer win or bust
        if dealer_wins(dealer_total, player_total):
            print('\033[1;31;47m ################ GAME RESULT ########################\033[0;0m')
            print('Dealer wins!!')
            c.lose_bet(bet_value)
            print('Player Bust -  lost the game!!!')
            # print('########################################')
            chips_total_value = c.balance
            break
        else:
            dealer_card = deck.pick_card()
            print(Card(dealer_card[0], dealer_card[1]))
            dealer_total = dealer_total + get_rank_value(dealer_card)
            continue

    chips_total_value = c.balance
    print('Player chips balance now: ' + str(c.balance))

    if play_again():
        continue
    else:
        print("See you later in the game")
        break

