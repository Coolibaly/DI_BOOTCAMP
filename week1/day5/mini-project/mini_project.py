# game.py - Game Class

import random


class Game:

    # Get user input (with validation)
    def get_user_item(self):

        valid_items = ["rock", "paper", "scissors"]

        while True:
            user_item = input("Choose rock, paper, or scissors: ").lower()

            if user_item in valid_items:
                return user_item
            else:
                print("Invalid choice. Try again.")

    # Get computer random choice
    def get_computer_item(self):

        return random.choice(["rock", "paper", "scissors"])

    # Determine game result
    def get_game_result(self, user_item, computer_item):

        if user_item == computer_item:
            return "draw"

        if (
            (user_item == "rock" and computer_item == "scissors") or
            (user_item == "scissors" and computer_item == "paper") or
            (user_item == "paper" and computer_item == "rock")
        ):
            return "win"

        return "loss"

    # Play one full game
    def play(self):

        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        print(f"You selected {user_item}. The computer selected {computer_item}.")

        if result == "win":
            print("You win!")
        elif result == "loss":
            print("You lose!")
        else:
            print("It's a draw!")

        return result