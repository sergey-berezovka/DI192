import random

class Game:
    def __init__(self):
        self.valid_items = ["rock", "paper", "scissors"]

    def get_user_item(self):
        while True:
            user_input = input("Choose rock, paper, or scissors: ").lower().strip()
            if user_input in self.valid_items:
                return user_input
            print("Invalid choice. Please try again.")

    def get_computer_item(self):
        return random.choice(self.valid_items)

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"

        winning_cases = {
            "rock": "scissors",
            "paper": "rock",
            "scissors": "paper"
        }

        if winning_cases[user_item] == computer_item:
            return "win"
        return "loss"

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()

        result = self.get_game_result(user_item, computer_item)

        print(f"\nYou chose: {user_item}")
        print(f"Computer chose: {computer_item}")
        print(f"Result: {result.upper()}\n")

        return result