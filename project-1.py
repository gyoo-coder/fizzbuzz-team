# Indian Poker
#
import random
import time

def suffle(d):
    suffled=random.sample(d,len(d))
    return suffled
rand= random.randint(1,100)
random.seed(rand)
deck = [i for i in range(1,11)]*2
cpu = 0
player = 0
chips = 20
round=0

while True:
    while chips!=0:
        round +=1
        print("--------------------------------")
        print(f"{round} round")
        time.sleep(1)
        if not len(deck)==0:
            # 1. 덱 셔플
            print("--------------------------------")
            print("Shuffle the deck.")
            deck=suffle(deck)
            time.sleep(1)
            print("--------------------------------")

            # 2. 카드 분배
            cpu =deck[-1]
            del deck[-1]
            print("The opponent will take the card.")
            time.sleep(1)
            print("--------------------------------")

            player = deck[-1]
            del deck[-1]
            print("The player takes the cards.")
            time.sleep(1)
            print("--------------------------------")
            #3. 카드 확인
            time.sleep(1)
            print("--------------------------------")
            print(f"Check the opponent's card.")
            print("--------------------------------")
            time.sleep(1)
            print("◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆")
            print(f"The opponent's card is {cpu}.")
            print("◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆")
            time.sleep(1)
            while True:
                bet = int(input(f"Enter the number of chips to bet on (DIE = 0) [Current chips: {chips}]"))
                if bet>chips:
                    time.sleep(1)
                    print("--------------------------------")
                    print(f"You cannot bet more than the chips you have. [Current chips: {chips}]")
                    continue
                elif bet<0:
                    time.sleep(1)
                    print("--------------------------------")
                    print(f"You cannot bet less than 0. [Current chips: {chips}]")
                    print(f"If you want to give up this game, please enter '0'" )
                    continue
                elif bet == 0:
                    time.sleep(1)
                    print(f"You gave up on this game." )
                    break
                elif bet<=chips:
                    chips -= bet
                    print(f"Bet {bet} chips.")
                    break
            if bet == 0:
                bet=0
                print(f"Restart the game.")
                time.sleep(1)
                break
            else:
                time.sleep(1)
                print("--------------------------------")
                print("The opponent accepted the bet.")
                print("--------------------------------")
                time.sleep(1)
                print("Check the results...3")
                time.sleep(1)
                print("Check the results...2")
                time.sleep(1)
                print("Check the results...1")
                time.sleep(1)

                print(f"---Opponent--------------player card-----")
                print(f"-----[{cpu}]--------------------[{player}]----")
                time.sleep(1)
                if cpu>player:
                    print(f"It's your defeat. Lost {bet} chips and currently holding chips {chips}chips")
                elif cpu==player:
                    chips += bet
                    print(f"It's a draw. You've got {bet} chips back, and you've got {chips}chips ")
                elif cpu<player:
                    chips += bet*2
                    print(f"It's your victory. You have won {bet} chips. You currently have chips {chips}chips ")



        else:
            #카드 덱 교체
            deck = [i for i in range(1, 11)] * 2
            print("Replace the deck.")
            time.sleep(1)
    if bet==0:
        continue
    else:
        print(f"You went bankrupt. Exit the game. You end in {round} Round")
    break

