import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print(logo)
def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

replay = 'y'
def sum_cards(x):
    sum_cards =0
    for i in x:
        sum_cards +=i
    return sum_cards

while replay == 'y':

    player_cards = []
    host_cards = []

    sum_host_cards = 0
    sum_player_cards = 0
    for i in range(2):
        player_cards.append(deal_card())
        host_cards.append(deal_card())
    # print(player_cards, host_cards)
    print(f'Your current cards are {player_cards}')
    sum_player_cards = sum_cards(player_cards)
    sum_host_cards = sum_cards(host_cards)
    if sum_player_cards ==11:
        if sum_host_cards != 11:
            print ('You won!')
        else: print('Equal!. Host also got blackjack')
    elif sum_host_cards == 11:
        print('The host got blackjack.You lost')
    draw = input('Do you want to draw another card? Enter Y or N  >>  ').lower()
    while draw == 'y':
        if draw == 'y':
            player_cards.append(deal_card())
            print(f'Your current cards: {player_cards} ')
            draw = input('Do you want to draw another card? Enter Y or N  >>  ').lower()
        else: pass
    sum_player_cards = sum_cards(player_cards)
    sum_host_cards = sum_cards(host_cards)
    if sum_player_cards > 21:
        print('Your cards got over 21 points, you lost')
    elif sum_player_cards > sum_host_cards:
        print(f'Here are the host card {host_cards}. You got higher points, you won!')
    elif sum_player_cards == sum_host_cards:
        print(f'Here are the host card {host_cards}. You got equal points!')
    else:
        print(f'Here are the host card {host_cards}. You lost')
    replay = input('Do you want to replay? Enter Y or N  >>  ').lower()