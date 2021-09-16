import random
from art import logo, vs
from game_data import data
import os

def format_data(account):
    '''format acc data into printable form'''
    account_name = account['name']
    account_desc = account['description']
    account_country = account['country']
    return(f"{account_name}, a {account_desc} from {account_country}.")

def check_answer(guess, a_followers, b_followers):
    """Use if statement to check if correct"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

# Driver
score = 0
should_continue = True
# Generate randon data
account_b = random.choice(data)

# Make game repeatable 
while should_continue:
    # Clear screen
    os.system("cls")
    
    # Print logo
    print(logo)

    # Generate randon data
    # Make position of account B the next position A
    account_a = account_b
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")

    # Ask user to guess
    guess = input("Who has more followers? 'A' or 'B' ").lower()

    
    # Get follow acc of each acc
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    # Check if user is correct
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Give user feedback and track score
    if is_correct:
        # Score keeping
        score +=1
        print(f"you're right! Current score: {score}")
    else:
        print(f"Sorry you're wrong! Final score: {score}")
        should_continue = False
