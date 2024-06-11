import os
#START
#show logo from art.py
#Ask for name input
#Ask for bid price
#Add name and bid in a dictionary as key and value respectively
#Are there other user to bid
#If YES clear screen and start all over
#If NO create a fuunction to check for the highest bidder
bid = {}
bidding_finished = False

def highest_bidder(bidding_record):
    highest_bid = 0
    for person in bidding_record:
        bid_amount = bidding_record[person]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = person
    print(f"The winner is {winner} with a bid of £{highest_bid}")


while not bidding_finished:
    name = input("What is your name? ")
    bid_price = int(input("How much are you bidding? £"))
    bid[name]=bid_price
    bidders=input("Are there any other bidders? Type 'Yes' or 'No' ").lower()
    if bidders == "no":
        bidding_finished = True
        highest_bidder(bid)
    elif bidders == "yes":
        os.system("cls||clear")
