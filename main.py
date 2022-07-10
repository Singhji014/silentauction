import os
from art import logo

print(logo)

repeat = False

auction_list ={}


def find_winner(bids):
    highest_bid = 0
    winner = ""
    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"Congratulation to {winner} for the highest bid of ${highest_bid}")



while not repeat:
    name = input("Enter your name: ")
    bids = int(input("Please enter your bids: $"))
    auction_list[name] = bids    
    more = input("Are there more bidders? (y/n): ")
    if more == "n":
        repeat = True
        find_winner(auction_list)
    elif more == "y":
        os.system("cls")
    
    
