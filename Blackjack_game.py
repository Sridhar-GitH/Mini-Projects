import random
import replit


def deal_cards():
    """return a random card"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate(cards):
    """calculating the cards from suitable game conditions"""
    if len(cards) == 2 and sum(cards) == 21:
        return 0
    if 11 in cards and sum(cards) < 21:
        cards.append(1)
        cards.remove(11)

    return sum(cards)


def compare(user_score, computer_score):
    """comparing the scores and give the results"""

    if computer_score > 21 and user_score > 21:
        return "you loses the game '-(".title()
    if computer_score == user_score:
        return 'draw the match ;0'.title()
    elif computer_score == 0:
        return 'computer is blackjack }('.title()
    elif user_score == 0:
        return 'the game is your side ;) BLACKJACK'.title()
    elif user_score > 21:
        return 'you went hard ;('.title()
    elif computer_score > 21:
        return 'you winsss... ;)'.title()
    elif computer_score < user_score <= 21:
        return 'you nailed it ! :)'.title()
    else:
        return 'simply you lose :('.title()


def black_jack():
    user_cards = []
    computer_cards = []
    Game_over = False

    for _ in range(2):
        """getting first two cards"""
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while not Game_over:

        user_score = calculate(cards=user_cards)
        computer_score = calculate(cards=computer_cards)

        print(f'user first cards are : {user_cards} and score is : {user_score}'.title())
        print(f'computer first cards is : [{computer_cards[0]}]'.title())

        if user_score == 0 or computer_score == 0 or user_score > 21:
            Game_over = True
        else:
            user = input('\ndo want to get another card [y/n]: '.title()).lower()
            if user == 'y':
                user_cards.append(deal_cards())
            else:
                Game_over = True

    """it's time for playing computer"""
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate(cards=computer_cards)
    print(f'user final cards are : {user_cards} and score is : {user_score}'.title())
    print(f'computer final cards are : {computer_cards} and score is {computer_score}'.title())
    print(compare(user_score, computer_score))


while input('\ndo you want to play the game blackjack [y/n] : '.title()).lower() == 'y':
    replit.clear()
    print("""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
""")

    black_jack()
