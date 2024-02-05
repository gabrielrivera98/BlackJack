from art import logo
import os
import sys

import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
begin = True

while begin:
    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if start == 'n':
        begin = False
        print("Have a good day!")
        sys.exit()
    os.system('cls')
    print(logo)

    # Player Starting Cards
    playerCardList = []
    playerTotal = 0
    for card in range(0, 2):
        cardNum = random.randint(0, len(cards) - 1)
        playerCardList.append(cardNum)
        playerTotal += cardNum

    # PC Starting Cards
    pcCardList = []
    pcTotal = 0
    for card in range(0, 2):
        cardNum = random.randint(0, len(cards) - 1)
        pcCardList.append(cardNum)
        pcTotal += cardNum

    print(f"Your cards: {playerCardList}")
    print(f"Computer's first card: {pcCardList[0]}")

    addCard = True
    while addCard:
        play = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if play == 'y':
            card = cards[random.randint(0, len(cards) - 1)]
            playerCardList.append(card)
            print(f"Your cards: {playerCardList}")
            playerTotal += card
        else:
            addCard = False

    os.system('cls')
    print(logo)
    print(f"Pc's cards: {pcCardList} Score: {pcTotal}\nPlayer cards: {playerCardList} Score: {playerTotal}")

    if playerTotal > 21:
        print("You went over. You lose!")
    elif playerTotal > pcTotal and playerTotal <= 21:
        print("You won!")
    elif pcTotal > playerTotal:
        print("You lose!")
    elif playerTotal == pcTotal:
        print("Tie!")
