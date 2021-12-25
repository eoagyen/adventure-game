import time
import random


def print_pause(message):
    print(message)
    time.sleep(2)


def intro(enemy, weapon):
    print_pause(f"Rumor has it that a {enemy} is somewhere around here, "
                "and has been terrifying the nearby village.")
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause(f"In your hand you hold your {weapon}.")


def valid_input(enemy, weapon, weapon2):
    choice = input("\nEnter 1 to knock on the door of the house.\n"
                   "Enter 2 to peer into the cave.\n"
                   "What would you like to do?\n"
                   "(Please enter 1 or 2).\n")
    while choice != "1" and choice != "2":
        choice = input("(Please enter 1 or 2).\n")
    if choice == "1":
        house(enemy, weapon, weapon2)
    elif choice == "2":
        cave(enemy, weapon, weapon2)


def house(enemy, weapon, weapon2):
    print_pause("You approach the door of the house.")
    print_pause(f"You are about to knock when the "
                f"door opens and out steps a {enemy}.")
    print_pause(f"Oh no! This is the {enemy}'s house!")
    print_pause(f"The {enemy} attacks you!")
    print_pause(f"You have a {weapon}.")
    fight = input("Do you want to fight? \"yes\" or \"no\"?: ")
    while fight != "yes" and fight != "no":
        fight = input("Do you want to fight? \"yes\" or \"no\"?: ")
    if fight == "yes":
        outcome(enemy)
    elif fight == "no":
        print_pause("You run away!")
        valid_input(enemy, weapon, weapon2)


def cave(enemy, weapon, weapon2):
    print_pause("You move cautiously into the cave.")
    print_pause("It turns out to be only a very small cave.")
    print_pause(f"Your eye sees a {weapon2} behind a rock.")
    print_pause(f"You have found a {weapon2}!")
    print_pause("You walk back out to the field.")
    field(enemy, weapon, weapon2)


def field(enemy, weapon, weapon2):
    print_pause(f"You have a {weapon2} now.")
    weapon = weapon2
    valid_input(enemy, weapon, weapon2)


def win(enemy):
    print_pause(f"You stand up to the {enemy} and you have defeated it")
    print_pause("You win!")


def lose(enemy):
    print_pause(f"Ouch! You were not lucky. The {enemy} has killed you.")
    print_pause("GAME OVER!")


def outcome(enemy):
    outcomes = ["win", "lose"]
    outcome = random.choice(outcomes)
    if outcome == "win":
        win(enemy)
    elif outcome == "lose":
        lose(enemy)


def play_game():
    enemies = ["troll", "bear", "dragon", "dinosaur",
               "elephant", "tiger", "lion"]
    weapons = ["dagger", "sword", "sniper",
               "bow and arrow", "shortgun", "trusty"]
    for enemy in enemies:
        enemy = random.choice(enemies)
        break
    for weapon in weapons:
        weapon = random.choice(weapons)
        break
    for weapon2 in weapons:
        weapon2 = random.choice(weapons)
        break
    intro(enemy, weapon)
    valid_input(enemy, weapon, weapon2)
    play_again(enemy, weapon, weapon2)


def play_again(enemy, weapon, weapon2):
    restart_game = input("\nWould you like to play again? (y/n): ")
    if restart_game == "y":
        play_game()
    elif restart_game == "n":
        print_pause("\nThanks for playing and hope you enjoyed the game.")
    else:
        play_again(enemy, weapon, weapon2)


play_game()
