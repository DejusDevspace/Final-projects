import random
def deal_card():
    """ Returns a random card from the deck """
    cards =  [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    dealer_cards = random.choice(cards)
    return dealer_cards

def calculate_score(cards):
    """ Take a list of cards and return the score calculated from the cards"""
#hint 7
    if sum(cards) == 21 and len(cards) == 2:
        return 0
#hint 8    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)   

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw!!"
    elif computer_score == 0:
        return "You LOSE (Opponent has Blackjack)!!"
    elif user_score == 0:
        return "You WIN(Blackjack)!!"
    elif user_score > 21:
        return "You went over, You LOSE!!"
    elif computer_score > 21:
        return "Opponent went over, You WIN!!"
    elif user_score > computer_score:
        return "You WIN!!"
    else:
        return "You LOSE!!"

def play_game():

    user_card = []
    computer_card = []
    is_game_over = False

    for _ in range(2):
        # new_card = deal_card()
        user_card.append(deal_card())
        computer_card.append(deal_card())


    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f"Your cards: {user_card}, current score: {user_score}")
        print(f"Computer's first card: {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            cont_game = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if cont_game == "y":
                user_card.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)


    print(f"Your final hand: {user_card}, final score :{user_score}")
    print(f"Computer's final hand: {computer_card}, final score :{computer_score}")
    print(compare(user_score, computer_score))
    
#Hint 14
 
while input("Do you want to play a game of blackjack? 'y' or 'n': ").lower()   == "y":
    #os.system("cls||clear")
    play_game()